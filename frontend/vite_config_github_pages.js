import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Configuration Vite pour GitHub Pages
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  
  // Configuration pour GitHub Pages
  base: '/veille-academique/',  // Nom de votre repository
  
  // Configuration du build
  build: {
    outDir: 'dist',  // Dossier de sortie
    assetsDir: 'assets',
    
    // Optimisations pour le déploiement
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['lucide-react']
        }
      }
    }
  },
  
  // Configuration du serveur de développement
  server: {
    port: 5173,
    host: true
  },
  
  // Configuration pour la prévisualisation
  preview: {
    port: 4173,
    host: true
  }
})

