tinymce.init({
  selector: "textarea",  // change this value according to your HTML
  plugins: "image",
  menubar: "insert",
  toolbar: "image",
  image_class_list: [
    {title: 'Нет', value: ''},
    {title: 'Dog', value: 'dog'},
    {title: 'Cat', value: 'cat'}
  ]
});