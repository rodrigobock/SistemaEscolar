$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/listar_aluno',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(aluno) {
        for (var i in aluno) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + aluno[i].nome + '</td>' +
                '<td>' + aluno[i].email + '</td>' +
                '<td>' + aluno[i].cpf + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#tabelaAluno').append(lin);
        }
    }
});