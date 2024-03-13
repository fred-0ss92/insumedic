var tblClient;

function getData () {
    tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {
                "data": "id",
                "render": function (data, type, row) {
                    var color = '#' + Math.floor(Math.random()*16777215).toString(16); // Generar un color hexadecimal aleatorio
                    return '<div style="width: 30px; height: 30px; border-radius: 50%; background-color: ' + color + '; color: white; text-align: center; line-height: 30px;">' + row.nombre.charAt(0) + '</div>';
                }
            },
            {
                "data": null,
                "render": function (data, type, row) {
                    return '<span style="color: blue; font-weight: bold;">' + row.nombre + ' ' + row.apellidos + '</span><br><span style="color: #888888;">' + '<i class="bi bi-buildings"></i>  ' + row.nombre_empresa + '</span>';
                }
            },
            {"data": "cel"},
            {"data": "mail"},
            {"data": "direc"},
            {"data": "tel_empresa"},
            //{"data": "estado_deuda"},
            {
                "data": "estado_deuda",
                "render": function (data, type, row){
                    if (row.estado_deuda == "SIN DEUDA"){
                        return '<span style = "color: green; font-weight: bold;">' + row.estado_deuda + '</span>';
                    }
                    else{
                        return '<span style = "color: red; font-weight: bold;">' + row.estado_deuda + '</span>';
                    }
                }
            },
            
            {"data": "estado_deuda"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a title = "Ver historial de compras" href="#" rel="detalle" type="button" class="btn btn-secondary btn-xs btn-flat"><i class="bi bi-clock-history"></i></a> ';
                    buttons += '<a href="/admins/dlte01__clientes_personal/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += ' <a type="button" class="btn btn-primary btn-xs btn-flat"><i class="bi bi-pencil-square"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
};

$(function () {
    modal_title = $('.modal-title');

    getData();

});
