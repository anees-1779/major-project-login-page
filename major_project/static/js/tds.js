const videoInputs = document.querySelectorAll('.video-input');

videoInputs.forEach((input, index) => {
  input.addEventListener('change', function() {
    const reader = new FileReader();
    const videoElement = document.getElementById(`video${index + 1}`);

    reader.addEventListener('load', () => {
      videoElement.src = reader.result;
      videoElement.style.display = 'block'; // Show the video
    });

    reader.readAsDataURL(this.files[0]);
  });
});

msg = document.querySelectorAll('.msg') 
console.Log(msg.text)