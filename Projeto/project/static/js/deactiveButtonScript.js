document.getElementById("botao").disabled = true;
document.getElementById("input").addEventListener("input", function(event){

    //busca conteúdo do input
      var conteudo = document.getElementById("input").value;
  
      //valida conteudo do input 
      if (conteudo !== null && conteudo !== '') {
        //habilita o botão
        document.getElementById("botao").disabled = false;
      } else {
        //desabilita o botão se o conteúdo do input ficar em branco
        document.getElementById("botao").disabled = true;
      }
  });