$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/boletim',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(boletim) {
        for (var i in boletim) { //i vale a posição no vetor
            lin =
                '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + boletim[i].aluno.nome + '</td>' +
                '<td>' + boletim[i].aluno.email + '</td>' +
                '</tr>' +
                '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + boletim[i].disciplina.nome + '</td>' +
                '<td>' + boletim[i].disciplina.ementa + '</td>' +
                '<td>' + boletim[i].disciplina.ch + '</td>' +
                '</tr>' +
                '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + boletim[i].av1 + '</td>' +
                '<td>' + boletim[i].av2 + '</td>' +
                '<td>' + boletim[i].av3 + '</td>' +
                '<td>' + boletim[i].mediaFinal + '</td>' +
                '</tr>'

            // adiciona a linha no corpo da tabela
            $('#tabelaBoletim').append(lin);
        }
    }
});
