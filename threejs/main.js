const renderer = new THREE.WebGLRenderer();
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x00ffff, 1);
document.body.appendChild(renderer.domElement);

const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
camera.position.set(0, 0, 100);
camera.lookAt(0, 0, 0);

const scene = new THREE.Scene();

const controls = new THREE.OrbitControls(camera, renderer.domElement);

//controls.update() must be called after any manual changes to the camera's transform
camera.position.set(0, 20, 100);
controls.update();

const raycaster = new THREE.Raycaster()
const mouse = new THREE.Vector2();
const sceneMeshes = [];
const material = new THREE.MeshNormalMaterial();
const coneGeometry = new THREE.ConeGeometry(0.05, 0.2, 8)
const arrowHelper = new THREE.ArrowHelper(
  new THREE.Vector3(),
  new THREE.Vector3(),
  10,
  0xffff00
)
scene.add(arrowHelper)
console.log(sceneMeshes)

// TEXT ON THREE.JS CANVAS
// //create a blue LineBasicMaterial
// const material = new THREE.LineBasicMaterial({ color: 0x0000ff });

// const points = [];
// points.push(new THREE.Vector3(- 10, 0, 0));
// points.push(new THREE.Vector3(0, 10, 0));

// const geometry = new THREE.BufferGeometry().setFromPoints(points);

// const line = new THREE.Line(geometry, material);

// const loader = new FontLoader();

// let font = await loader.loadAsync(
//     "https://threejs.org/examples/fonts/helvetiker_regular.typeface.json"
//   );
// const textGeometry = new TextGeometry('Hello three.js!', {
//     font: font,
//     size: 10,
//     height: 5,
//     curveSegments: 12,
//     bevelEnabled: true,
//     bevelThickness: 10,
//     bevelSize: 8,
//     bevelOffset: 0,
//     bevelSegments: 5
// });
// textGeometry.center()
// let textMesh = new THREE.MeshBasicMaterial({ color: "aqua", wireframe: true });
// let text = new THREE.Mesh(textGeometry, textMesh);
// scene.add(line);
// scene.add(text);
// renderer.render(scene, camera);

// LOADING A 3D MODEL
// Instantiate a loader
const loader = new THREE.FBXLoader();
loader.crossOrigin = "";

// Optional: Provide a DRACOLoader instance to decode compressed mesh data
// const dracoLoader = new THREE.DRACOLoader();
// dracoLoader.setDecoderPath('https://cdn.jsdelivr.net/npm/three@0.139.2/examples/js/libs/draco/');
// loader.setDRACOLoader(dracoLoader);

var light = new THREE.DirectionalLight("#c1582d", 1);
var ambient = new THREE.AmbientLight("#85b2cd");
light.position.set(0, -70, 100).normalize();
scene.add(light);
scene.add(ambient);

// const hlight = new THREE.AmbientLight(0x888888,100);
// scene.add(hlight);

// const directionalLight = new THREE.DirectionalLight(0xffffff,100);
// directionalLight.position.set(0,1,0);
// directionalLight.castShadow = true;
// scene.add(directionalLight);

// const light = new THREE.PointLight(0xc4c4c4,10);
// light.position.set(0,300,500);
// scene.add(light);

// const light2 = new THREE.PointLight(0xc4c4c4,10);
// light2.position.set(500,100,0);
// scene.add(light2);

// const light3 = new THREE.PointLight(0xc4c4c4,10);
// light3.position.set(0,100,-500);
// scene.add(light3);

// const light4 = new THREE.PointLight(0xc4c4c4,10);
// light4.position.set(-500,300,500);
// scene.add(light4);

// const textureLoader = new THREE.TextureLoader();
// var texture = textureLoader.load('./Ch36_1001_Diffuse.png');
// texture.encoding = THREE.sRGBEncoding;
// texture.flipY = false

// Load a glTF resource
loader.load(
  // resource URL
  './Ch36_nonPBR.fbx',
  // called when the resource is loaded
  function (object) {
    // gltf.scene.traverse(function (child) {
    //   if (child instanceof THREE.Mesh) {
    //       const m = child
    //       m.receiveShadow = true
    //       m.castShadow = true;
    //       (m.material).flatShading = true
    //       sceneMeshes.push(m)
    //   }
      sceneMeshes.push(object)
      scene.add(object);
  //   })
  },
  // called while loading is progressing
  function (xhr) {

    console.log((xhr.loaded / xhr.total * 100) + '% loaded');

  },
  // called when loading has errors
  function (error) {

    console.log('An error happened');

  }
);

// renderer.domElement.addEventListener('mousemove', onMouseMove, false)
renderer.domElement.addEventListener('dblclick', onDoubleClick, false)

function onMouseMove() {
  console.log('a')
}
function onDoubleClick(event) {
  const mouse = {
    x: (event.clientX / renderer.domElement.clientWidth) * 2 - 1,
    y: -(event.clientY / renderer.domElement.clientHeight) * 2 + 1,
  }
  raycaster.setFromCamera(mouse, camera)

  // console.log(scene.children[2])
  // console.log(sceneMeshes)
  const intersects = raycaster.intersectObjects(scene.children)
  console.log('b',intersects)
  if (intersects.length > 0) {
    // console.log(intersects)
    const n = new THREE.Vector3()
    n.copy((intersects[0].face).normal)
    n.transformDirection(intersects[0].object.matrixWorld)

    arrowHelper.setDirection(n)
    arrowHelper.position.copy(intersects[0].point)
  }
}
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  // raycaster.setFromCamera(mouse, camera);
  // var intersects = raycaster.intersectObjects(scene, true)
  // if (intersects.length > 0) {
  //   console.log(intersects)
  // }
  renderer.render(scene, camera);
}
animate();
