const colors = require('tailwindcss/colors')

module.exports = {
  purge: { content: ["./public/**/*.html", "./src/**/*.vue"] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      body: ['Neue Machina', 'sans-serif'],
    },
    colors: {
      'background': '#F5EDE3',
      'green': '#8AA49D',
      'black': '#000000'
    },
    fontSize: {
      'tiny': '1rem',
      'xs': '1.125rem',
      'sm': '1.25rem',
      'md': '1.5rem',
      'lg': '1.75rem',
      'xl': '1.875rem',
      '2xl': '2rem',
      '3xl': '2.25rem',
      '4xl': '3rem',
      '5xl': '5.375rem',
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
