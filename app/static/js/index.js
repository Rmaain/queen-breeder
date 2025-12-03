document.body.addEventListener("click", (env) => {
    const isExandableTitle = !!env.target.closest('.expandable--title')
    const expandable = env.target.closest('.expandable')
    if(!isExandableTitle){
        return
    }
    expandable.classList.toggle('expandable--open')
})


hive_container = document.getElementById('hive')
add_btn = document.getElementById('add_frame')

add_btn.addEventListener('click', () => {
    const index = hive_container.children.length
    const NewFrame = document.createElement('div')
    NewFrame.classList.add('frame')
    NewFrame.innerHTML = ` 
    <label>Quadro ${ index+1 }</label>
    <input type="file" name="frames-${index+1}-image" accept="image/*" ></input>
    `
    hive_container.appendChild(NewFrame)
})
