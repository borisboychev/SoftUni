function highlight() {
    if (this.className.includes("highlighted")) {
        this.className = this.className.replace("highlighted", '');
    } else {
        this.className += ' highlighted';
    }
}

window.onload = function(){
    [...document.getElementsByClassName('highlightable')]
        .forEach(el => {
            console.log(el);
            el.addEventListener('mouseenter', highlight);
            el.addEventListener('mouseout', highlight);
        });
}
