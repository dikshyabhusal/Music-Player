document.addEventListener('DOMContentLoaded', function () {
    const playButtons = document.querySelectorAll('.play-btn');
    const prevButtons = document.querySelectorAll('.prev-btn');
    const nextButtons = document.querySelectorAll('.next-btn');
    const audioPlayers = document.querySelectorAll('.audio-player');

    let currentAudioIndex = 0; // Track the currently playing audio

    // Function to play audio
    function playAudio(index) {
        audioPlayers.forEach((audio, i) => {
            if (i === index) {
                audio.play();
                playButtons[i].innerHTML = '<i class="fa fa-pause"></i> Pause';
            } else {
                audio.pause();
                audio.currentTime = 0; // Reset other audio
                playButtons[i].innerHTML = '<i class="fa fa-play"></i> Play';
            }
        });
        currentAudioIndex = index;
    }

    // Function to pause audio
    function pauseAudio(index) {
        const audio = audioPlayers[index];
        audio.pause();
        playButtons[index].innerHTML = '<i class="fa fa-play"></i> Play';
    }

    // Play/Pause Button Logic
    playButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            const audio = audioPlayers[index];
            if (audio.paused) {
                playAudio(index);
            } else {
                pauseAudio(index);
            }
        });
    });

    // Previous Button Logic
    prevButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            const prevIndex = (index - 1 + audioPlayers.length) % audioPlayers.length; // Cycle to the last song if at the first
            playAudio(prevIndex);
        });
    });

    // Next Button Logic
    nextButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            const nextIndex = (index + 1) % audioPlayers.length; // Cycle to the first song if at the last
            playAudio(nextIndex);
        });
    });
});
