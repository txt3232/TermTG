function downloadFile() {
    fetch('main.py')
        .then(response => response.text())
        .then(content => {
            const blob = new Blob([content], {type: 'text/x-python'});
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'main.py';
            link.click();
            URL.revokeObjectURL(link.href);
        });
}
