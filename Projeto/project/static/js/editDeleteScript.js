function ActiveDelete(){
    let divModal = document.getElementById("divModalDelete");
    
    divModal.classList.remove("deactive");
}

function ActiveEdit(){
    let divModal = document.getElementById("divModalEdit");
    
    divModal.classList.remove("deactive");
}

function CancelButton(){
    let divModalDelete = document.getElementById("divModalDelete");
    let divModalEdit = document.getElementById("divModalEdit");
    
    if(divModalDelete.classList.contains("deactive")){
        divModalEdit.classList.add("deactive");
    }else{
        divModalDelete.classList.add("deactive");
    }
}