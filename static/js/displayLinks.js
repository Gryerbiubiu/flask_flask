// displayLinks.js

// Fetch the JSON data from links.json
fetch('{{ url_for("static", filename="links.json") }}')
    .then(response => response.json())
    .then(data => displayLinks(data));

// Function to display links in the specified container
function displayLinks(data) {
    const pythonContainer = document.getElementById('pythonContainer');
    const aiContainer = document.getElementById('aiContainer');
    const specialContainer = document.getElementById('specialContainer');
    const dataContainer = document.getElementById('dataContainer');

    // Iterate through categories
    data.categories.forEach(category => {
        // Iterate through items in the category
        category.items.forEach(item => {
            // Create a link item for each item
            const linkItem = document.createElement('div');
            linkItem.className = 'link-item';

            // Create a link for each item
            const link = document.createElement('a');
            link.href = item.link;
            link.target = '_blank';
            link.textContent = item.name;

            // Append the link to the link item
            linkItem.appendChild(link);

            // Append the link item to the corresponding container based on category
            switch (category.name) {
                case 'Python':
                    pythonContainer.appendChild(linkItem);
                    break;
                case 'AI':
                    aiContainer.appendChild(linkItem);
                    break;
                case 'Special':
                    specialContainer.appendChild(linkItem);
                    break;
                case 'Data':
                    dataContainer.appendChild(linkItem);
                    break;
                default:
                    break;
            }
        });
    });
}
