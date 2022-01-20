$(function () { // quando o documento estiver pronto/carregado

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirPessoa", function () {
        //pegar dados da tela
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        cpf = $("#campoCPF").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, email: email, cpf: cpf });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_aluno',
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
                $("#campoNome").val("");
                $("#campoEmail").val("");
                $("#campoCPF").val("");
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