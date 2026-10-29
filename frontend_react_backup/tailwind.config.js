/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#EEF4FF',
          100: '#DCEAFE',
          200: '#BDD7FD',
          300: '#91BFFB',
          400: '#5E9EF6',
          500: '#347BEF',
          600: '#2457C5', // Primary brand deep professional blue
          700: '#1D459E',
          800: '#1B3B82',
          900: '#172B4D', // Primary dark navy
        },
        surface: {
          ground: '#F6F8FC', // Soft cool white background
          card: '#FFFFFF',
          border: '#E2E8F0',
          subtle: '#EDF2F7',
        },
        navy: {
          900: '#0F1D33',
          800: '#172B4D',
          700: '#263D66',
        },
        slateText: {
          primary: '#172B4D',
          secondary: '#526179',
          muted: '#7A8B9E',
        },
        state: {
          success: '#0F7B42',
          successBg: '#E8F7EE',
          warning: '#B56804',
          warningBg: '#FEF6E7',
          error: '#D92D20',
          errorBg: '#FEF3F2',
          info: '#2457C5',
          infoBg: '#DCEAFE',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      boxShadow: {
        'subtle': '0 1px 3px 0 rgba(16, 24, 40, 0.06), 0 1px 2px 0 rgba(16, 24, 40, 0.04)',
        'card': '0 4px 6px -1px rgba(16, 24, 40, 0.05), 0 2px 4px -2px rgba(16, 24, 40, 0.05)',
        'card-hover': '0 10px 15px -3px rgba(16, 24, 40, 0.08), 0 4px 6px -4px rgba(16, 24, 40, 0.04)',
      }
    },
  },
  plugins: [],
}

