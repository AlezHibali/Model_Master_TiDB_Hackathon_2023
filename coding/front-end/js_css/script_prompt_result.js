document.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  const response = urlParams.get('response');

  if (response) {
    const responseContainer = document.createElement('div');

    // Extracting Model_List and display it after 'Related Models'
    const responseParts = response.split('Model_List:');
    const responseData = responseParts[0].trim().replace(/'/g, ''); // Remove single quotes
    const modelListData = responseParts[1] ? responseParts[1].trim() : '';

    if (responseData) {
      if (response.startsWith('Error:')) {
        const errorMessage = response.replace('Error:', '').trim();
        alert(`Error: ${errorMessage}`);
        return; // Stop further processing if there's an error
      }
      
      const responseItems = responseData.split('\n');

      responseItems.forEach(item => {
        const responseCard = document.createElement('div');
        responseCard.classList.add('response-card');

        // Extracting 'downloads_last_month' and 'model_name'
        const data = item.replace(/Response: |{|}/g, ''); // Remove unnecessary characters
        const keyValuePairs = data.split(',');

        const leftColumn = document.createElement('div');
        leftColumn.classList.add('left-column');

        const rightColumn = document.createElement('div');
        rightColumn.classList.add('right-column');

        let modelName = '';

        keyValuePairs.forEach(keyValue => {
          const [key, value] = keyValue.split(':');

          if (key.trim() === 'model_name') {
            modelName = value.trim();
          } else {
            // Creating separate cards for each attribute and value
            const attributeCard = document.createElement('div');
            attributeCard.classList.add('attribute-card');
            attributeCard.innerText = `${key.trim()}`;

            const valueCard = document.createElement('div');
            valueCard.classList.add('value-card');
            valueCard.innerText = `${value.trim()}`;

            // Appending attribute and value cards to the respective columns
            leftColumn.appendChild(attributeCard);
            rightColumn.appendChild(valueCard);
          }
        });

        // Display 'model name' if it exists
        if (modelName !== '') {
          const modelNameCard = document.createElement('div');
          modelNameCard.classList.add('attribute-card');
          modelNameCard.innerText = 'model name';

          const modelNameValueCard = document.createElement('div');
          modelNameValueCard.classList.add('value-card');
          modelNameValueCard.innerText = modelName;

          leftColumn.insertBefore(modelNameCard, leftColumn.firstChild);
          rightColumn.insertBefore(modelNameValueCard, rightColumn.firstChild);
        }

        // Appending columns and a middle line to the response card
        responseCard.appendChild(leftColumn);
        responseCard.appendChild(createMiddleLine());
        responseCard.appendChild(rightColumn);

        // Append each response card to the response container
        responseContainer.appendChild(responseCard);
      });
    }

    // Inserting the response container before 'Related Models' heading
    const relatedModelsHeading = document.querySelector('.heading-2');
    relatedModelsHeading.parentNode.insertBefore(responseContainer, relatedModelsHeading);

    if (modelListData) {
      const modelListContainer = document.createElement('div');
      const modelNames = modelListData.split(',');

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
      relatedModelsHeading.parentNode.appendChild(modelListContainer);
    }
  }
});

function createMiddleLine() {
  const middleLine = document.createElement('div');
  middleLine.classList.add('middle-line');
  return middleLine;
}