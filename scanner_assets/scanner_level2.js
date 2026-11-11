// C2 level 2: historical mechanical geometry on the accepted C2 contact path.
const scannerFixed = new THREE.Group(), scannerMobile = new THREE.Group();
scene.add(scannerFixed, scannerMobile);
const scannerFixedParts = [], scannerMobileParts = [];
let scannerExploded = false, scannerShown = true, scannerRun = null;
let scannerLast = 0, scannerSent = 0, scannerCameraMode = 'overview';
let scannerShellOpacity = 1;
let scannerUTContrast = true;
function scannerMesh(d) {
  return new THREE.Mesh(geo(d.V, d.F), new THREE.MeshStandardMaterial({
    color: new THREE.Color(...d.color), roughness: .7, side: THREE.DoubleSide
  }));
}
for (const [id, d] of Object.entries(SCANNER6.shells)) {
  const mesh = scannerMesh(d); mesh.name = id;
  scannerFixed.add(mesh); scannerFixedParts.push([mesh, d]);
}
for (const [id, d] of Object.entries(SCANNER6.parts)) {
  const mesh = scannerMesh(d); mesh.name = id;
  scannerMobile.add(mesh); scannerMobileParts.push([mesh, d]);
}
function scannerPose(p) {
  scannerMobile.position.set(...p.contact);
  scannerMobile.quaternion.setFromRotationMatrix(new THREE.Matrix4().makeBasis(
    new THREE.Vector3(...p.across), new THREE.Vector3(...p.along), new THREE.Vector3(...p.normal)));
  scannerFixedParts.forEach(([o,d]) => o.position.set(...(scannerExploded ? d.exploded_offset_world_mm : [0,0,0])));
  scannerMobileParts.forEach(([o,d]) => o.position.set(...(scannerExploded ? d.exploded_offset_local_mm : [0,0,0])));
  scannerFixed.visible = scannerShown; scannerMobile.visible = scannerShown;
  contactGroup.visible = !scannerShown && document.getElementById('holder').checked;
  moving.visible = false;
  // Exploded offsets are illustrative: never let a neighbouring blade appear
  // to be the support for a displaced scanner component.
  for(let i=0;i<base.length;i++)if(DATA.base[i].name.startsWith('Voisine'))
    base[i].visible = !scannerExploded && document.getElementById('neighbors').checked;
}
const scannerPriorContact = contactGeometry;
contactGeometry = function(p) { scannerPriorContact(p); scannerPose(p); };
function scannerContextMaterials() {
  restoreBladeVisibility();
  renderer.localClippingEnabled = true;
  for (let i=0; i<base.length; i++) {
    const material = base[i].material;
    material.clippingPlanes = []; material.clipIntersection = false;
    material.side = THREE.DoubleSide; material.needsUpdate = true;
    if (DATA.base[i].name.startsWith('Voisine')) {
      base[i].visible = !scannerExploded && document.getElementById('neighbors').checked;
      material.color.set(DATA.base[i].name.includes('verte') ? '#248757' : '#3559ae');
      material.opacity = .3;
    }
  }
  document.getElementById('alpha').value = .3;
}
const scannerPriorFrame = updateContactFrame;
updateContactFrame = function(m) {
  const keep = scannerRun ? displayPose : null;
  const view = contactMode === 'three' ? {az,el,radius,target:target.clone()} : null;
  scannerPriorFrame(m);
  if (keep) contactGeometry(keep);
  scannerPose(displayPose);
  scannerApplyUTContrast();
  if (view) {
    az=view.az; el=view.el; radius=view.radius; target.copy(view.target);
    scannerContextMaterials();
  }
};
const scannerBar = document.createElement('div');
scannerBar.style = 'padding:6px 9px;display:flex;gap:6px;flex-wrap:wrap;align-items:center';
contactControls.before(scannerBar);
const scannerShow = document.createElement('button'), scannerExplode = document.createElement('button');
const scannerContext = document.createElement('button'), scannerDetail = document.createElement('button');
const scannerShellLabel = document.createElement('label'), scannerShellText = document.createElement('span');
const scannerShellSlider = document.createElement('input');
scannerShellSlider.type='range'; scannerShellSlider.min='.15'; scannerShellSlider.max='1';
scannerShellSlider.step='.05'; scannerShellSlider.value='1'; scannerShellSlider.style.width='80px';
scannerShellLabel.append(scannerShellText,scannerShellSlider);
scannerBar.append(scannerShow,scannerExplode,scannerContext,scannerDetail,scannerShellLabel);
const scannerContrastLabel=document.createElement('label'),scannerContrastText=document.createElement('span');
const scannerContrastInput=document.createElement('input');
scannerContrastInput.type='checkbox';scannerContrastInput.checked=true;scannerContrastInput.id='c2UTContrast';
scannerContrastLabel.append(scannerContrastInput,scannerContrastText);scannerBar.append(scannerContrastLabel);
function scannerApplyUTContrast(){
  liveFan.material.opacity=scannerUTContrast ? .62 : .22;
  liveShot.material.size=scannerUTContrast?6:3;
  cloudP.material.size=scannerUTContrast?4.5:2.7;
  for(const object of indications.children){
    if(object.isSprite)object.scale.set(scannerUTContrast?30:22,scannerUTContrast?10:7,1);
    else if(object.isMesh)object.scale.setScalar(scannerUTContrast?1.6:1);
  }
}
scannerContrastInput.onchange=()=>{scannerUTContrast=scannerContrastInput.checked;scannerApplyUTContrast();scannerText()};
function scannerText() {
  scannerShow.textContent=text(scannerShown?'Masquer le scanner':'Afficher le scanner',scannerShown?'Hide scanner':'Show scanner');
  scannerExplode.textContent=text(scannerExploded?'Assembler le scanner':'Éclater le scanner',scannerExploded?'Assemble scanner':'Explode scanner');
  scannerContext.textContent=text('Scanner entre les aubes','Scanner between blades');
  scannerDetail.textContent=text('Détail PA et guidage','PA and guide detail');
  scannerShellText.textContent=text('Opacité des coques','Shell opacity');
  scannerContrastText.textContent=text('Contraste UT renforcé','Enhanced UT contrast');
  document.getElementById('childTitle').textContent=text('C2 — Niveau 2 · aube et scanner','C2 — Level 2 · blade and scanner');
  document.getElementById('warning').textContent=text(
    'N2-R02 — Scan et projet de scanner acceptés par l’auteur ; revue de l’affichage UT. Codeur simulé.',
    'N2-R02 — Replay and scanner concept accepted by the author; UT display under review. Simulated encoder.');
  c2DisplayNote.textContent=scannerExploded?text(
    'VUE ÉCLATÉE — pièces décalées pour explication, hors position de fonctionnement. Aubes voisines masquées.',
    'EXPLODED VIEW — parts offset for illustration, outside operating positions. Adjacent blades hidden.'):
    text('SCANNER ASSEMBLÉ — appui sur l’aube centrale ; balayage C2 EXTRADOS → INTRADOS.',
    'ASSEMBLED SCANNER — contact on the central blade; C2 EXTRADOS → INTRADOS scan.');
  if(scannerUTContrast)c2DisplayNote.textContent+=text(
    ' Taille des repères et contraste renforcés ; amplitudes et coordonnées inchangées.',
    'Larger markers and enhanced contrast; amplitudes and coordinates unchanged.');
}
scannerShow.onclick=()=>{scannerShown=!scannerShown;scannerPose(displayPose);scannerText()};
scannerExplode.onclick=()=>{scannerExploded=!scannerExploded;scannerPose(displayPose);scannerText()};
scannerShellSlider.oninput=()=>{
  scannerShellOpacity=+scannerShellSlider.value;
  for(const [o] of scannerFixedParts){o.material.opacity=scannerShellOpacity;o.material.transparent=scannerShellOpacity<1;o.material.depthWrite=scannerShellOpacity===1;o.material.needsUpdate=true}
};
function scannerContextView() {
  scannerCameraMode='overview';modeContact('three');scannerContextMaterials();
  target.set(35,150,55);az=-.64;el=.5;radius=440;scannerPose(displayPose);
}
function scannerDetailView() {
  scannerCameraMode='detail';modeContact('three');scannerContextMaterials();
  const p=displayPose,n=new THREE.Vector3(...p.normal);
  const view=n.clone().addScaledVector(new THREE.Vector3(...p.along),.5).normalize();
  target.copy(new THREE.Vector3(...p.contact)).addScaledVector(n,10);
  az=Math.atan2(view.y,view.x);el=Math.asin(view.z);radius=160;
  scannerPose(displayPose);
}
scannerContext.onclick=scannerContextView;scannerDetail.onclick=scannerDetailView;
threeButton.onclick=scannerDetailView;
const scannerPriorLang=langScene;
langScene=function(l){scannerPriorLang(l);scannerText()};
document.getElementById('holder').addEventListener('change',()=>scannerPose(displayPose));
document.getElementById('neighbors').addEventListener('change',()=>scannerPose(displayPose));
window.addEventListener('message',e=>{
  if(e.source!==parent)return;
  const m=e.data;
  if(m?.type==='C2_SCANNER_RUN'){
    glideJob=null;motionJob=null;
    if(scannerExploded){scannerExploded=false;scannerText()}
    scannerRun={direction:m.direction===-1?-1:1,speed:Math.max(.1,Math.min(20,+m.speed||5)),
      distance:distanceAtPhase(displayPose.phase),lastShot:Math.min(199,Math.floor(displayPose.phase+1e-8)+1)};
    scannerLast=0;scannerPose(displayPose);
  }else if(m?.type==='C2_SCANNER_STOP')scannerRun=null;
  else if(m?.type==='C2_SCANNER_SPEED'&&scannerRun)scannerRun.speed=Math.max(.1,Math.min(20,+m.speed||5));
  else if(m?.type==='C2_GLIDE_PLAY'||m?.type==='C2_CONTACT_MOVE'){
    scannerRun=null;
    if(scannerExploded){scannerExploded=false;scannerPose(displayPose);scannerText()}
  }
});
function scannerLoop(t){
  scannerExplode.disabled=!!scannerRun||!!glideJob||!!motionJob;
  const dt=scannerLast?Math.min(.1,(t-scannerLast)/1000):0;scannerLast=t;
  if(scannerRun){
    const job=scannerRun;
    job.distance=Math.max(0,Math.min(CONTACT.contact_arc_lengths.at(-1),job.distance+job.direction*job.speed*dt));
    const phase=phaseAtDistance(job.distance);glidePhase=phase;
    contactGeometry(poseOnSkin(phase));drawContactSection();
    if(beamMode==='planes')drawBeamPlanes();
    else if(contactMode==='three'){
      const positions=[];for(const ray of displayRays(displayPose))positions.push(...ray.entry,...ray.end);
      liveFanGeo.setAttribute('position',new THREE.Float32BufferAttribute(positions,3));
      liveFanGeo.computeBoundingSphere();liveFan.visible=true;
      liveShot.visible=false; // Stored samples belong to an acquired pose, never the in-between pose.
    }
    const shot=Math.min(199,Math.floor(phase+1e-8)+1);
    if(shot!==job.lastShot){job.lastShot=shot;parent.postMessage({type:'C2_SCANNER_SHOT',shot},'*')}
    if((job.direction<0&&job.distance<=0)||(job.direction>0&&job.distance>=CONTACT.contact_arc_lengths.at(-1))){
      scannerRun=null;parent.postMessage({type:'C2_SCANNER_END'},'*');
    }
  }
  if(t-scannerSent>120){scannerSent=t;parent.postMessage({type:'C2_SCANNER_POSITION',phase:displayPose.phase,
    distance:distanceAtPhase(displayPose.phase),total:CONTACT.contact_arc_lengths.at(-1),running:!!scannerRun},'*')}
  requestAnimationFrame(scannerLoop);
}
window.C2Scanner={get audit(){return {release:'N2-R02',shells:scannerFixed.children.length,
  mobileParts:scannerMobile.children.length,phase:displayPose.phase,distance:distanceAtPhase(displayPose.phase),
  running:!!scannerRun,sourcePathUnchanged:true,shown:scannerShown,exploded:scannerExploded,
  cameraMode:scannerCameraMode,shellOpacity:scannerShellOpacity,
  enhancedUTContrast:scannerUTContrast,liveShotSize:liveShot.material.size,rayOpacity:liveFan.material.opacity,
  neighboursShown:base.filter((o,i)=>DATA.base[i].name.startsWith('Voisine')).map(o=>o.visible),
  contactPositionErrorMm:scannerMobile.position.distanceTo(new THREE.Vector3(...displayPose.contact)),
  rotationDeterminant:new THREE.Matrix4().makeRotationFromQuaternion(scannerMobile.quaternion).determinant(),
  cutPlanes:base.map(o=>o.material.clippingPlanes?.length||0)}},context:scannerContextView,detail:scannerDetailView};
scannerContextView();scannerApplyUTContrast();scannerText();requestAnimationFrame(scannerLoop);
