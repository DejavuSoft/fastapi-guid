/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",                           // обязательно, если есть index.html
    "./src/**/*.{vue,js,ts,jsx,tsx}",         // все файлы в src и вложенных папках
    // если у тебя есть другие папки с классами — добавь
    // "./public/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}