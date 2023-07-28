document.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  const response = urlParams.get('response');

  if (response) {
    const responseParagraph = document.querySelector('.paragraph-large.bg-neutral-700');
    const modelListContainer = document.createElement('div');

    // Extracting Model_List and display it after 'Related Models'
    const responseParts = response.split('Model_List:');
    const responseData = responseParts[0].trim();
    const modelListData = responseParts[1] ? responseParts[1].trim() : '';

    // Displaying Response in the paragraph without the word "Response"
    responseParagraph.innerText = responseData.replace('Response: ', '');

    if (modelListData) {
      const modelNames = modelListData.split(',');

      const parentContainer = document.querySelector('.w-layout-blockcontainer.container.w-container');

      // Creating cards for each model with clickable links
      modelNames.forEach(modelName => {
        const modelCard = document.createElement('div');
        modelCard.classList.add('model-card');

        const modelTitle = document.createElement('h2');
        modelTitle.classList.add('model-title');
        modelTitle.innerText = modelName;

        // Adding event listener to make the entire card clickable
        modelCard.addEventListener('click', function() {
          const modelLink = `https://model-master.webflow.io/model/${modelName.toLowerCase()}`; // for local
          // const modelLink = `model/${modelName.toLowerCase()}`;  // for public
          window.location.href = modelLink;
        });

        modelCard.appendChild(modelTitle);
        modelListContainer.appendChild(modelCard);
      });

      // Inserting Model_List container after 'Related Models' heading
      parentContainer.appendChild(modelListContainer);
    }
  }
});