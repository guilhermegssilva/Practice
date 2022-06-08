const daysEl = document.getElementById("days")
const hoursEl = document.getElementById("hours")
const minutesEl = document.getElementById("minutes")
const secondsEl = document.getElementById("seconds")

const nextYear = (new Date().getFullYear() + 1).toString()
const newYear = `1 jan ${nextYear}`


function countdown() {
    const currentDate = new Date()
    const newYearDate = new Date(newYear)
    const base = Math.floor((newYearDate - currentDate) / 1000)

    const days = Math.floor(base / 3600 / 24)
    const hours = Math.floor((base / 3600) % 24)
    const minutes = Math.floor((base / 60) % 60)
    const seconds = Math.floor(base % 60)

    daysEl.innerHTML = formatTime(days)
    hoursEl.innerHTML = formatTime(hours)
    minutesEl.innerHTML = formatTime(minutes)
    secondsEl.innerHTML = formatTime(seconds)
} 

function formatTime(time) {
    return time < 10?`0${time}`: time
}

setInterval(countdown, 1000)

countdown()