const videoElement = document.getElementById('webcam');
const captureButton = document.getElementById('capture-btn');
const canvasElement = document.getElementById('canvas');
const capturedPhotoElement = document.getElementById('captured-photo');
const canvasContext = canvasElement.getContext('2d');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    videoElement.srcObject = stream;
  })
  .catch(err => {
    console.log('Error accessing webcam: ', err);
  });

captureButton.addEventListener('click', () => {
  canvasElement.width = videoElement.videoWidth;
  canvasElement.height = videoElement.videoHeight;
  
  canvasContext.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
  
  const dataUrl = canvasElement.toDataURL('image/png');
  capturedPhotoElement.src = dataUrl;
});
