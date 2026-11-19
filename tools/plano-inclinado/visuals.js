/* SVGs are generated from the same physical state as the controls. */
const InclineVisuals = (() => {
  'use strict';
  const C={ink:'#243f35',muted:'#64736b',ramp:'#e4e9dc',weight:'#b04a2b',normal:'#286b90',force:'#72519a',tension:'#946300',speed:'#286b90',accel:'#72519a'};
  const fmt=(x,d=2)=> (Math.abs(x)<1e-9?0:x).toLocaleString('pt-BR',{maximumFractionDigits:d});
  const pt=p=>p.map(x=>+x.toFixed(3)).join(',');
  const add=(p,d,k=1)=>[p[0]+d[0]*k,p[1]+d[1]*k];
  const txt=(x,y,t,size=16,color=C.ink,anchor='middle')=>`<text x="${x}" y="${y}" font-size="${size}" fill="${color}" text-anchor="${anchor}">${t}</text>`;
  const line=(a,b,color=C.ink,width=2,extra='')=>`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="${color}" stroke-width="${width}" ${extra}/>`;
  function arrow(p,vector,color,label='',dashed=false){
    const len=Math.hypot(...vector); if(len<.05)return '';
    const end=add(p,vector), u=vector.map(v=>v/len), perp=[-u[1],u[0]], head=Math.min(9,len*.4);
    return line(p,end,color,3,dashed?'stroke-dasharray="5 4"':'')+`<polygon points="${pt(end)} ${pt(add(add(end,u,-head),perp,head*.5))} ${pt(add(add(end,u,-head),perp,-head*.5))}" fill="${color}"/>`+(label?txt(end[0]+perp[0]*13+u[0]*12,end[1]+perp[1]*13+u[1]*12+5,label,17,color):'');
  }
  function svg(body,desc,w=720,h=400){return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" role="img" aria-label="${desc}" style="font-family:Arial,Helvetica,sans-serif"><title>${desc}</title>${body}</svg>`;}
  function block(p,angle,label){return `<g transform="translate(${p}) rotate(${angle})"><rect x="-18" y="-18" width="36" height="36" rx="3" fill="#fffef9" stroke="${C.ink}" stroke-width="2"/></g>`+txt(p[0],p[1]+5,label,15);}
  function motion(z,prompt=false){
    const {p}=z; let b='';
    if(z.kind==='tablePulley'||z.kind==='hangingPulley'){
      const r=InclinePhysics.rope(z), c=z.cosine,s=z.sine, rad=z.angle*180/Math.PI;
      if(z.kind==='tablePulley'){
        const Q=[358,140+c*4], end=add(Q,[c,s],310), touch=[360+s*14,140-c*14];
        b=`<path d="M70 144 H${Q[0]} L${pt(end)} V345 H70 Z" fill="${C.ramp}" stroke="${C.ink}" stroke-width="2"/>`;
        b+=`<path d="M${pt(add(r.A,[1,0],18))} L360 126 A14 14 0 0 1 ${pt(touch)} L${pt(add(r.B,[c,s],-18))}" fill="none" stroke="${C.tension}" stroke-width="3"/>`;
        b+=`<circle cx="360" cy="140" r="14" fill="none" stroke="${C.ink}" stroke-width="2"/>`+block(r.A,0,'A')+block(r.B,rad,'B');
        b+=txt(155,70,prompt?`mA = ${fmt(p.massA)} kg`:'A → polia',16)+txt(550,135,prompt?`mB = ${fmt(p.massB)} kg`:'B ↓ rampa',16)+txt(605,325,'30°',16);
        if(!prompt){b+=arrow(add(r.A,[0,-1],47),[z.v*11,0],C.speed,'vA')+arrow(add(r.B,[s,-c],55),[c*z.v*11,s*z.v*11],C.speed,'vB');}
      }else{
        const n=[-s,-c],u=[c,-s],Q=add(r.pulley,n,-4),bottom=add(Q,u,-480),touch=add(r.pulley,n,14);
        b=`<path d="M${pt(bottom)} L${pt(Q)} L${Q[0]},${bottom[1]} Z" fill="${C.ramp}" stroke="${C.ink}" stroke-width="2"/>`;
        b+=`<path d="M${pt(add(r.M,u,18))} L${pt(touch)} A14 14 0 0 1 554 90 L554 ${r.m[1]-18}" fill="none" stroke="${C.tension}" stroke-width="3"/>`;
        b+=`<circle cx="540" cy="90" r="14" fill="none" stroke="${C.ink}" stroke-width="2"/>`+block(r.M,-rad,'M')+block(r.m,0,'m')+txt(bottom[0]+62,bottom[1]-12,'30°',16);
        if(!prompt)b+=arrow(add(r.M,n,52),[-c*z.v*15,s*z.v*15],C.speed,'vM')+arrow(add(r.m,[1,0],50),[0,-z.v*15],C.speed,'vm');
        if(prompt)b+=arrow(add(r.M,n,52),[-c*65,s*65],C.accel,'a = 2 m/s²');
      }
      if(!prompt)b+=txt(360,380,`Mesmo fio: deslocamentos de módulo ${fmt(Math.abs(z.s))} m`,16);
    }else{
      const u=[z.cosine,-z.sine],n=[-z.sine,-z.cosine],bottom=[160,325],L=Math.min(390,205/z.sine),top=add(bottom,u,L);
      b=`<path d="M${pt(bottom)} L${pt(top)} L${top[0]},325 Z" fill="${C.ramp}" stroke="${C.ink}" stroke-width="2"/>`;
      const fraction=z.kind==='forces'?.48:z.kind==='down'?1-z.s/z.distance:z.s/z.distance;
      const pos=add(add(bottom,u,L*fraction),n,20);
      b+=block(pos,-z.angle*180/Math.PI,'');
      const angleLabel=z.id===6&&prompt?'θ':(z.id===1||z.id===2)&&Math.abs(z.sine-.6)<1e-8?'37°':`θ ≈ ${fmt(z.angle*180/Math.PI,1)}°`;
      b+=txt(bottom[0]+90,310,z.id===5?`sen θ = h/L = ${fmt(z.sine)}`:angleLabel,16);
      if(z.kind==='down'){
        b+=txt(top[0]+20,top[1]-14,'A',19)+txt(bottom[0]-18,bottom[1]+20,'B',19);
        b+=txt((top[0]+bottom[0])/2+42,(top[1]+325)/2+35,`L = ${fmt(p.length)} m`,17);
        if(z.id===5)b+=txt(top[0]+28,(top[1]+325)/2,`h = ${fmt(p.height)} m`,16,C.ink,'start');
      }else if(z.kind==='up'){
        b+=txt(top[0]+20,top[1]-14,z.id===6?'C':'B',19)+txt(bottom[0]-14,350,z.id===6?'B':'A',19);
        if(z.id===6)b+=line([35,325],bottom)+txt(48,350,'A',18)+arrow([50,300],[65,0],C.speed,'v₀');
        if(prompt)b+=arrow(add(pos,n,38),u.map(x=>x*80),C.speed,z.id===6?'v₀':'v₀ = 12 m/s');
      }
      if(z.id===4 && prompt)b+=arrow(add(pos,u,25),u.map(x=>x*80),C.force,'F = 22 N');
      if(!prompt && z.kind!=='forces'){
        const sign=z.kind==='down'?-1:1, dir=u.map(x=>x*sign), maxV=z.kind==='up'?p.v0:z.a*z.duration;
        b+=arrow(add(pos,n,40),dir.map(x=>x*75*z.v/maxV),C.speed,'v');
        b+=arrow(add(pos,n,85),dir.map(x=>x*55*Math.sign(z.a)),C.accel,'a');
        b+=txt(360,380,z.kind==='up'&&z.progress===1?'v = 0 na parada; a continua para baixo.':`s = ${fmt(z.s)} m   ·   t = ${fmt(z.t)} s`,16);
      }
    }
    const desc=`Questão ${z.id}: ${z.kind.includes('Pulley')?'dois blocos unidos por um fio ideal':'bloco sobre plano inclinado'}. ${prompt?'Esquema do enunciado.':`Deslocamento ${fmt(z.s)} m; velocidade ${fmt(z.v)} m/s.`}`;
    return svg(b,desc);
  }
  function forces(z,components=false,staged=false){
    const p=z.p, dual=z.kind.includes('Pulley'); let panels=[];
    const ramp=(mass,sine,cosine,u,n,extra,label)=>({mass,sine,cosine,u,n,extra,label});
    if(z.kind==='tablePulley'){
      panels=[ramp(p.massA,0,1,[1,0],[0,-1],[['T',[1,0],z.tension]],'Bloco A · horizontal'),ramp(p.massB,z.sine,p.cosine,[z.cosine,z.sine],[z.sine,-z.cosine],[['T',[-z.cosine,-z.sine],z.tension]],'Bloco B · descida')];
    }else if(z.kind==='hangingPulley'){
      panels=[ramp(z.massLarge,z.sine,z.cosine,[-z.cosine,z.sine],[-z.sine,-z.cosine],[['T',[z.cosine,-z.sine],z.tension]],'Bloco M · rampa'),{mass:p.massSmall,extra:[['T',[0,-1],z.tension]],label:'Bloco m · suspenso'}];
    }else{
      panels=[ramp(p.mass||1,z.sine,z.cosine,[-z.cosine,z.sine],[-z.sine,-z.cosine],z.id===4?[['F',[z.cosine,-z.sine],p.force]]:[],'Eixos paralelo e perpendicular à rampa')];
    }
    const scale=104/Math.max(...panels.map(v=>v.mass*p.g),...panels.flatMap(v=>v.extra.map(e=>e[2])));
    const rendered=panels.map(f=>{
      let b='';const x=180,o=[x,170],W=f.mass*p.g, stage=staged?z.stage:3;
      b+=txt(x,26,f.label,17)+`<circle cx="${x}" cy="170" r="7" fill="${C.ink}"/>`;
      if(f.u){b+=line(add(o,f.u,-85),add(o,f.u,85),'#c5cdc1',1)+line(add(o,f.n,-85),add(o,f.n,85),'#c5cdc1',1);}
      // The projections replace P in the force sum; P remains a dashed reference only.
      b+=`<g opacity="${components&&f.u&&stage>=1?.28:1}">`+arrow(o,[0,W*scale],C.weight,'P',components&&!!f.u&&stage>=1)+'</g>';
      if(components&&f.u&&stage>=1){b+=arrow(o,f.u.map(v=>v*W*f.sine*scale),C.weight,'P∥',true)+arrow(o,f.n.map(v=>-v*W*f.cosine*scale),C.weight,'P⊥',true);}
      if(f.n&&stage>=2)b+=arrow(o,f.n.map(v=>v*W*f.cosine*scale),C.normal,'N');
      if(stage>=2)for(const [label,dir,value] of f.extra)b+=arrow(o,dir.map(v=>v*value*scale),label==='T'?C.tension:C.force,label);
      const numeric=dual||p.mass;
      b+=txt(x,316,numeric?`P = ${fmt(W)} N${f.n?`   ·   N = ${fmt(W*f.cosine)} N`:''}`:'P = mg   ·   N = mg cos θ',16);
      if(stage>=3)b+=txt(x,345,dual?`T = ${fmt(z.tension)} N`:`Fᵣ/m = a = ${fmt(z.a)} m/s²`,16,C.force);
      return svg(b,`Diagrama de forças da questão ${z.id}, ${f.label}. ${components?'Peso decomposto: as projeções substituem P, não são novas forças.':'Forças reais: peso, normal quando há contato e força aplicada ou tração quando presente.'}`,360,370);
    });
    return `<div class="force-panels${dual?' dual':''}">${rendered.join('')}</div>`;
  }
  function graph(z){
    const initial=z.kind==='up'?z.p.v0:0, final=initial+z.a*z.duration;
    const max=Math.max(1,Math.abs(initial),Math.abs(final)), x=t=>65+590*t/z.duration;
    const zero=final<0?65:230, y=v=>zero-v/max*155;
    let b=line([65,35],[65,255])+line([65,zero],[675,zero]);
    b+=txt(30,25,'v (m/s)',15)+txt(671,282,'t (s)',15)+txt(65,282,'0',14)+txt(655,282,fmt(z.duration),14);
    b+=`<path d="M65 ${zero} L65 ${y(initial)} L${x(z.t)} ${y(z.v)} L${x(z.t)} ${zero} Z" fill="#dce8ee"/>`;
    b+=line([65,y(initial)],[655,y(final)],C.speed,3)+line([x(z.t),zero],[x(z.t),y(z.v)],C.muted,1,'stroke-dasharray="4 4"');
    b+=`<circle cx="${x(z.t)}" cy="${y(z.v)}" r="6" fill="${C.speed}"/>`+txt(360,315,`Área até t = deslocamento: ${fmt(z.s)} m`,16);
    return svg(b,`Velocidade em função do tempo. A inclinação é a aceleração ${fmt(z.a)} m/s². Área assinada até o instante atual: ${fmt(z.s)} m.`,720,330);
  }
  return {fmt,motion,forces,graph};
})();
