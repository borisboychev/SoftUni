function expandCollapse() {
    if (this.parentElement.className.indexOf('collapsed') >= 0) {
        this.parentElement.className =
            this.parentElement.className.replace('collapsed', '');
    } else {
        this.parentElement.className += ' collapsed';
    }
}

function initExpand() {
    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', expandCollapse);
    });
}

function changeState() {
    if (this.className === 'done') {
        this.innerHTML = 'Not Done';
        this.className = 'not-done';
    } else {
        this.innerHTML = 'Done';
        this.className = 'done';
    }

}

function initState() {
    const items = [...document.getElementsByClassName('todo-state')]
    items.forEach(item => {
        item.childNodes[1].addEventListener('click', changeState);
    })
}

initExpand();
initState();