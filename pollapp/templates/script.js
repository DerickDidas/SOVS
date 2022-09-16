const video = document.getElementById('video')

function startVideo() {
    navigator.getUsermedia(
      { video: {} },
      stream => video.srcObject = stream,
      err => console.error(err)
    )
}


startVideo()