// 저장만 되고, 삭제는 안되는 이슈 해결하기.
const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input");
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos"

let toDos = [];

function saveToDo() {
    localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}


function deleteToDo(event) {
    const li = event.target.parentElement;
    li.remove();
    // filter 사용.
    toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
    // 이거 안하면 삭제한거 저장 안됨.
    saveToDo();
}

// newToDo가 object로 바뀌어서 수정해줘야함.
function paintToDo(newToDo) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    const button = document.createElement("button");
    
    // newToDo -> newToDo.text 로.
    li.id = newToDo.id;
    span.innerText = newToDo.text;
    button.innerText = "X";

    li.appendChild(span);
    li.appendChild(button);
    
    toDoList.appendChild(li);
    button.addEventListener("click", deleteToDo);
}

function handleToDoSubmit(event) {
    event.preventDefault();
    const newToDo = toDoInput.value;
    toDoInput.value = "";
    // 여기서 원소를 오브젝트로 바꿔서 지우고자 하는 애한테 이름을 달아줌.
    // toDos.push(newToDo);
    const newToDoObj = {
        text: newToDo,
        // 지금의 시간을 랜덤한 수로 주는거.
        id: Date.now(),
    }
    // paintToDo(newToDo);
    toDos.push(newToDoObj);
    paintToDo(newToDoObj);
    saveToDo();
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const saveToDos = localStorage.getItem(TODOS_KEY);

if (saveToDos) {
    const parsedToDos = JSON.parse(saveToDos);
    toDos = parsedToDos;
    parsedToDos.forEach(paintToDo);
}

// 사실 어레이에서 지우는건 걔만 빼고 새로 만드는거다.!
// 그 기능을 하는 함수 : filter(x){return x~} : 에 관련된 조건 x~를 만족하지 못하면. 추방!
