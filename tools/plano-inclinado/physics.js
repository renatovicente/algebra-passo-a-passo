/* One model for diagrams, playback, graphs and numerical readouts. SI units. */
const InclinePhysics = (() => {
  'use strict';
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  function state(q, input, progress = 0) {
    const p = {...input};
    if (q.id === 5) p.height = clamp(p.height, 1, Math.min(9.5, p.length - .5));
    const sine = q.id === 5 ? p.height / p.length : p.sine;
    const cosine = Math.sqrt(1 - sine * sine);
    const z = {id:q.id, kind:q.lab.kind, p, progress:clamp(progress,0,1), sine, cosine,
      angle:Math.asin(sine), g:p.g, mass:p.mass, duration:1, t:0, s:0, v:0};
    z.weight = p.mass ? p.mass*p.g : null;
    z.normal = z.weight === null ? null : z.weight*cosine;
    z.parallel = z.weight === null ? null : z.weight*sine;
    if (z.kind === 'forces') {
      z.a = q.id === 4 ? (p.force-z.parallel)/p.mass : p.g*sine;
      z.resultant = z.a*p.mass;
      z.stage = Math.min(3, Math.floor(z.progress*4));
    } else if (z.kind === 'down') {
      z.a = p.g*sine;
      z.distance = p.length;
      z.duration = Math.sqrt(2*z.distance/z.a);
      z.t = z.progress*z.duration;
      z.s = z.a*z.t*z.t/2;
      z.v = z.a*z.t;
    } else if (z.kind === 'up') {
      z.a = -p.g*sine;
      z.distance = p.v0*p.v0/(2*p.g*sine);
      z.duration = p.v0/(p.g*sine);
      z.t = z.progress*z.duration;
      z.v = Math.max(0, p.v0+z.a*z.t);
      z.s = p.v0*z.t+z.a*z.t*z.t/2;
      z.kinetic = z.v*z.v/2;
      z.potential = p.g*sine*z.s;
      z.energy = p.v0*p.v0/2;
    } else if (z.kind === 'tablePulley') {
      z.a = p.massB*p.g*sine/(p.massA+p.massB);
      z.tension = p.massA*z.a;
      z.t = z.progress;
      z.s = z.a*z.t*z.t/2;
      z.v = z.a*z.t;
    } else {
      z.massLarge = p.ratio*p.massSmall;
      z.a = p.g*(p.ratio*sine-1)/(p.ratio+1);
      z.tension = p.massSmall*(p.g+z.a);
      z.t = z.progress;
      z.s = z.a*z.t*z.t/2;
      z.v = z.a*z.t;
    }
    return z;
  }
  function rope(z) {
    const delta = 25*z.s, c=z.cosine, s=z.sine, r=14, half=18;
    if(z.kind==='tablePulley') {
      const pulley=[360,140], normal=[s,-c], down=[c,s];
      const A=[180+delta,126], B=[360+normal[0]*r+down[0]*(110+delta),140+normal[1]*r+down[1]*(110+delta)];
      return {pulley,A,B,delta,length:(360-(A[0]+half))+(110+delta-half)+r*z.angle};
    }
    const pulley=[540,90], normal=[-s,-c], up=[c,-s];
    const M=[540+normal[0]*r-up[0]*(220+delta),90+normal[1]*r-up[1]*(220+delta)], m=[554,240-delta];
    return {pulley,M,m,delta,length:(220+delta-half)+(m[1]-half-90)+r*(Math.PI/2+z.angle)};
  }
  return {state,rope,clamp};
})();
