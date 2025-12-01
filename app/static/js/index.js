document.body.addEventListener("click", (env) => {
    const isExandableTitle = !!env.target.closest('.expandable--title')
    const expandable = env.target.closest('.expandable')
    if(!isExandableTitle){
        return
    }
    expandable.classList.toggle('expandable--open')
})
