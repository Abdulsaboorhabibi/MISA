/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../MISA/**/*.{html,js}"
  ],
  theme: {
    extend: {
      daisyui: {
        themes: ["light", "dark", "cupcake"],
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

