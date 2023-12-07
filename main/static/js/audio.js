var audio = document.getElementById('audio');


var trigger = document.querySelectorAll('.aTriggers');
trigger.forEach(function(audioSingle){
    audioSingle.addEventListener('click', function(){
        // img.className = "active";
        var dataAudio = this.getAttribute('data-audio');
        var dataActive = this.getAttribute('data-active');
        audio.src = dataAudio;
        if (dataActive === "" || dataActive === "pause") {
            audio.load();
            audio.play();
            this.setAttribute("data-active", "active");
            this.innerHTML = '<i class="fa fa-pause"></i>';
        } else {
            audio.pause();
            this.setAttribute("data-active", "pause");
            this.innerHTML = '<i class="fa fa-play"></i>';
        }
    })
})

