// Add a custom menu to the active document, including a separator and a sub-menu
function onOpen(e) {
  DocumentApp.getUi()
      .createMenu('Recipes')
      .addItem('Recipe formatting', 'formatRecipe')
      .addItem('Clear', 'deleteBody')
      .addToUi();
}

// Format the recipe body
function formatRecipe() {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();
  
  var listType = DocumentApp.ElementType.LIST_ITEM;
  var listRangeElem = null;

  var paragraphType = DocumentApp.ElementType.PARAGRAPH;
  var paragraphRangeElem = null;

  body.replaceText("1/2", "½");
  body.replaceText("1/3", "⅓");
  body.replaceText("1/4", "¼");
  body.replaceText("1/5", "⅕");
  body.replaceText("1/6", "⅙");
  body.replaceText("1/8", "⅛");
  body.replaceText("2/3", "⅔");
  body.replaceText("3/4", "¾");
  body.replaceText("3/8", "⅜");
  body.replaceText("/", " / ");
  body.replaceText("  /  ", " / ");
  body.replaceText(" /  ", " / ");

  // Center the image
  paragraphRangeElem = body.findElement(paragraphType, paragraphRangeElem);
  var paragraphElem = paragraphRangeElem.getElement();
  paragraphElem.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  // Format the recipe title
  paragraphRangeElem = body.findElement(paragraphType, paragraphRangeElem);
  paragraphElem = paragraphRangeElem.getElement();
  paragraphElem.setAlignment(DocumentApp.HorizontalAlignment.CENTER);
  paragraphElem.setSpacingAfter(12);
  paragraphElem.setBold(true);

  // Add a space after the last bullet item
  while (listRangeElem = body.findElement(listType, listRangeElem)) {
    var listElem = listRangeElem.getElement();
    listElem.setSpacingBefore(0);
    listElem.setSpacingAfter(0);
    listElem.setLineSpacing(1.15);
  }
  listElem.setSpacingAfter(12);

  // Set spacing for recipe instructions
  while (paragraphRangeElem = body.findElement(paragraphType, paragraphRangeElem)) {
    paragraphElem = paragraphRangeElem.getElement();
    paragraphElem.setLineSpacing(1.5);
  }
}

// Clear the doc of all text and reset the line spacing
function deleteBody() {
  var doc = DocumentApp.getActiveDocument();
  doc.getBody().appendParagraph(" ").setLineSpacing(1.15);
  // doc.setName("Template");
  doc.clear();
}