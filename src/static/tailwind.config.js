module.exports = {
  content: ["../templates/**/*.html", "../core/templates/**/*.html"],
  theme: {
    container: {
      center: true,
      screens: {
        md: "1120px",
        lg: "1120px",
        xl: "1120px",
        "2xl": "1120px",
      }
    }
    ,
    extend: {
      colors: {
        'primary': '#E84545',
        'secondary': '#903749',
        'teritary': '#522546',
        'blog-dark': '#2B2E4A',
      }
    },
  },
  plugins: [],
}
