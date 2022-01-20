$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/listar_professor',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(professor) {
        for (var i in professor) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + professor[i].id + '</td>' +
                '<td>' + professor[i].nome + '</td>' +
                '<td>' + professor[i].email + '</td>' +
                '<td>' + professor[i].cpf + '</td>' +
                '<td>' + professor[i].disciplina + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#tabelaProfessor').append(lin);
        }
    }
});