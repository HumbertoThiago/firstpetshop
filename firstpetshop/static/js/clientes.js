const btnExcluir = document.querySelectorAll(".btn-excluir");
const btnDelete = document.querySelectorAll(".btn-execute-delete");

(function() {

    btnExcluir.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            Swal.fire({
                title: "Confirma a Exclusão ?",
                showCancelButton: true,
                confirmButtonText: "Excluir",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => { 
                    console.log(e.target.href);                    
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });
})();