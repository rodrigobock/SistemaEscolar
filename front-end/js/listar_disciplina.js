$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/listar_disciplina',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(disciplina) {
        for (var i in disciplina) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + disciplina[i].id + '</td>' +
                '<td>' + disciplina[i].nome + '</td>' +
                '<td>' + disciplina[i].ementa + '</td>' +
                '<td>' + disciplina[i].ch + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#tabelaDisciplina').append(lin);
        }
    }
});