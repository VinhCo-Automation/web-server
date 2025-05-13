document.querySelectorAll('.add-form').forEach(form => {
    form.addEventListener('submit', async e => {
        e.preventDefault();
        const table = form.dataset.table;
        const data = Object.fromEntries(new FormData(form).entries());

        const response = await fetch(`/add/${table}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) location.reload();
    });
});

function deleteRow(table, id, date, time) {
    fetch(`/delete/${table}?ID_Device=${id}&Date=${date}&Time=${time}`, {
        method: 'DELETE'
    }).then(res => {
        if (res.ok) location.reload();
    });
}
