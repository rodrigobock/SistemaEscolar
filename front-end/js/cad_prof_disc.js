$(function () { // quando o documento estiver pronto/carregado

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btnAddProfDisc", function () {
        //pegar dados da tela
        idProfessor = $("#idProfessor").val();
        idDisciplina = $("#idDisciplina").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ professor_id: idProfessor, disciplina_id: idDisciplina });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_professor_disciplina',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: pessoaIncluida, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function pessoaIncluida(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Pessoa incluída com sucesso!");
                // limpar os campos
                $("#idProfessor").val("");
                $("#idDisciplina").val("");
                location.reload();
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoIncluir(retorno) {
            // informar mensagem de erro
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });

});