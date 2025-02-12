document.querySelectorAll('.video-input').forEach((input, index) => {
  input.addEventListener('change', function () {
    const reader = new FileReader();
    const videoElement = document.getElementById(`video${index + 1}`);

    if (!videoElement) return; // Prevent errors if element is missing

    reader.addEventListener('load', () => {
      videoElement.src = reader.result;
      videoElement.style.display = 'block'; // Show the video
    });

    if (this.files.length > 0) {
      reader.readAsDataURL(this.files[0]);
    }
  });
});

// Generalized function to remove text and icon
const removeBg = (n) => {
  const removeTxt = document.getElementById(`rmvText${n}`);
  const removeIcon = document.getElementById(`rmvIcon${n}`);

  if (removeTxt) removeTxt.remove(); // Check if element exists before removing
  if (removeIcon) removeIcon.remove();
};
