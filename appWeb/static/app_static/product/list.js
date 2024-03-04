var tblClient;
var modal_title;

//agregar aqui para cambio de models
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
            {"data": "id"},
            {"data": "name"},
            {"data": "image"},
            {"data": "marca.marca"},
            {"data": "compra_pvp"},
            {"data": "pvp"},
            {"data": "exist"},
            {"data": "exist"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat btnEdit"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a href="#" rel="detalle" type="button" class="btn btn-secondary btn-xs btn-flat"><i class="fas fa-info-circle"></i></a> ';
                    return buttons;
                }
            },
            {
                targets: [-6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 30px; height: 30px;">';
                }             
            }
        ],
        initComplete: function (settings, json) {

        }
    });
};

$(function () {
    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un cliente');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
        $('#imagePreviewContainer').html(''); // Limpiar la vista previa de la imagen
    });

    $('#data tbody').on('click', 'a[rel="edit"]', function () {
        modal_title.find('span').html('Editar un producto');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="name"]').val(data.name);
        // No intentes establecer el valor del input file aquí
        $('textarea[name="desc"]').val(data.desc);
        $('input[name="fecha"]').val(data.fecha);
        $('input[name="compra_pvp"]').val(data.compra_pvp);
        $('select[name="marca"]').val(data.marca.id);
        $('select[name="provedor"]').val(data.provedor.id);
        $('input[name="pvp"]').val(data.pvp);
        $('input[name="exist"]').val(data.exist);
        $('#myModalClient').modal('show');

        // Agregar la vista previa de la imagen
        if (data.image) {
            var imagePreview = '<img src="' + data.image + '" style="max-width: 100px; max-height: 100px;" />';
            $('#imagePreviewContainer').html(imagePreview);
        } else {
            $('#imagePreviewContainer').html('No hay imagen seleccionada');
        }
    });

    $('#data tbody').on('click', 'a[rel="delete"]', function () {
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de borrar el producto del inventario?', parameters, function () {
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "Producto eliminado exitosamente",
                showConfirmButton: false,
                timer: 3000
              });
        });        
    });    

    $('#data tbody').on('click', 'a[rel="detalle"]', function () {
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        // Actualiza el contenido del modal con los datos del producto
        $('#productId').text(data.id);
        $('#productName').text(data.name);        
        $('#productDate').text(data.fecha);        
        $('#productProovedor').text(data.provedor);        
        $('#productdesc').text(data.desc);        
        // Muestra el modal
        $('#productDetailsModal').modal('show');
    });

    $('#myModalClient').on('shown.bs.modal', function () {});

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
        });
    });
});