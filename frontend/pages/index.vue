<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-sky-100 to-blue-200 flex flex-col justify-center items-center relative overflow-hidden">
    <!-- Enhanced background decorative elements -->
    <div class="absolute inset-0 overflow-hidden">
      <div class="absolute -top-1/2 -left-1/2 w-96 h-96 bg-gradient-to-r from-blue-300 to-sky-400 rounded-full mix-blend-multiply filter blur-xl opacity-60 animate-blob"></div>
      <div class="absolute -top-1/2 -right-1/2 w-96 h-96 bg-gradient-to-r from-sky-300 to-blue-400 rounded-full mix-blend-multiply filter blur-xl opacity-60 animate-blob animation-delay-2000"></div>
      <div class="absolute -bottom-1/2 left-1/2 w-96 h-96 bg-gradient-to-r from-blue-200 to-sky-300 rounded-full mix-blend-multiply filter blur-xl opacity-60 animate-blob animation-delay-4000"></div>
      
      <!-- Floating particles -->
      <div class="absolute top-1/4 left-1/4 w-4 h-4 bg-blue-400 rounded-full animate-float opacity-70"></div>
      <div class="absolute top-1/3 right-1/4 w-3 h-3 bg-sky-400 rounded-full animate-float animation-delay-1000 opacity-70"></div>
      <div class="absolute bottom-1/3 left-1/3 w-5 h-5 bg-blue-300 rounded-full animate-float animation-delay-2000 opacity-70"></div>
      <div class="absolute bottom-1/4 right-1/3 w-2 h-2 bg-sky-500 rounded-full animate-float animation-delay-3000 opacity-70"></div>
    </div>

    <!-- Main content -->
    <div class="relative z-10 text-center px-4 max-w-4xl mx-auto">

      <!-- Main welcome message -->
      <h1 class="text-6xl md:text-8xl font-bold mb-6 animate-fade-in-up animation-delay-300">
        <span class="bg-gradient-to-r from-blue-600 via-sky-500 to-blue-700 bg-clip-text text-transparent animate-gradient-x">
          Welcome to
        </span>
      </h1>
      
      <h2 class="text-5xl md:text-7xl font-bold mb-8 animate-fade-in-up animation-delay-600">
        <span class="bg-gradient-to-r from-sky-600 via-blue-600 to-sky-700 bg-clip-text text-transparent animate-gradient-x animation-delay-500">
          Youwei's Awesome
        </span>
      </h2>

      <h3 class="text-4xl md:text-6xl font-bold text-blue-800 mb-12 animate-fade-in-up animation-delay-900">
        <span class="relative">
          Storage Space
          <div class="absolute -bottom-2 left-0 right-0 h-1 bg-gradient-to-r from-blue-400 to-sky-400 rounded-full animate-expand"></div>
        </span>
      </h3>

      <!-- Animated subtitle -->
      <div class="text-xl md:text-2xl text-blue-700 mb-12 animate-fade-in-up animation-delay-1200 max-w-3xl mx-auto leading-relaxed space-y-2">
        <p class="animate-typewriter">
          Experience the future of cloud storage with seamless file management,
        </p>
        <p class="animate-typewriter animation-delay-1800">
          secure sharing, and lightning-fast access to your digital world.
        </p>
      </div>

      <!-- Enhanced feature showcase -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 animate-fade-in-up animation-delay-1500">
        <div class="group bg-gradient-to-br from-white/90 to-blue-50/80 backdrop-blur-md rounded-2xl p-8 shadow-xl hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 hover:rotate-1 border border-blue-100">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-400 to-sky-500 rounded-2xl flex items-center justify-center mb-6 mx-auto group-hover:scale-110 transition-transform duration-300 shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-blue-800 mb-3">Lightning Upload</h3>
          <p class="text-blue-600">Drag, drop, and watch your files soar to the cloud</p>
        </div>

        <div class="group bg-gradient-to-br from-white/90 to-sky-50/80 backdrop-blur-md rounded-2xl p-8 shadow-xl hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 hover:-rotate-1 border border-sky-100">
          <div class="w-16 h-16 bg-gradient-to-br from-sky-400 to-blue-500 rounded-2xl flex items-center justify-center mb-6 mx-auto group-hover:scale-110 transition-transform duration-300 shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-sky-800 mb-3">Smart Sharing</h3>
          <p class="text-sky-600">Connect and collaborate with intelligent file sharing</p>
        </div>

        <div class="group bg-gradient-to-br from-white/90 to-blue-50/80 backdrop-blur-md rounded-2xl p-8 shadow-xl hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 hover:rotate-1 border border-blue-100">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-sky-600 rounded-2xl flex items-center justify-center mb-6 mx-auto group-hover:scale-110 transition-transform duration-300 shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-blue-800 mb-3">Fort Knox Security</h3>
          <p class="text-blue-600">Your files are protected with military-grade encryption</p>
        </div>
      </div>

      <!-- Enhanced CTA Button -->
      <div class="animate-fade-in-up animation-delay-1800">
        <a href="https://github.com/AntoDono/ZhenCMS" 
           target="_blank"
           rel="noopener noreferrer"
           class="group relative inline-flex items-center px-10 py-5 bg-gradient-to-r from-blue-600 via-sky-500 to-blue-700 text-white font-bold rounded-2xl shadow-2xl hover:shadow-blue-500/25 transform hover:-translate-y-2 hover:scale-105 transition-all duration-500 text-xl overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-r from-sky-400 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          <svg class="relative z-10 w-6 h-6 mr-3 group-hover:rotate-12 transition-transform duration-300" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
          <span class="relative z-10">Visit GitHub</span>
          <div class="absolute inset-0 -z-10 bg-gradient-to-r from-blue-600 to-sky-600 blur-lg opacity-75 group-hover:opacity-100 transition-opacity duration-300"></div>
        </a>
      </div>

      <!-- Enhanced Footer -->
      <div class="mt-20 text-blue-600 text-lg animate-fade-in-up animation-delay-2100">
        <p class="flex items-center justify-center space-x-2">
          <span>Crafted with</span>
          <svg class="w-5 h-5 text-red-500 animate-heartbeat" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
          </svg>
          <span>by <a href="https://youweizhen.com" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 transition-colors">Youwei Zhen</a> • <a href="https://github.com/AntoDono/ZhenCMS" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 transition-colors">Open Source</a></span>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
// SEO and meta data for better embeds
useHead({
  title: 'ZhenCMS - Modern Cloud Storage & File Management',
  meta: [
    {
      name: 'description',
      content: 'ZhenCMS is a modern, secure cloud storage platform with seamless file management, intelligent sharing, and lightning-fast access. Built with Django and Nuxt.js by Youwei Zhen.'
    },
    {
      name: 'keywords',
      content: 'cloud storage, file management, file sharing, cms, django, nuxt.js, secure storage, youwei zhen'
    },
    {
      name: 'author',
      content: 'Youwei Zhen'
    },
    // Open Graph meta tags for better social media embeds
    {
      property: 'og:title',
      content: 'ZhenCMS - Modern Cloud Storage & File Management'
    },
    {
      property: 'og:description',
      content: 'Experience the future of cloud storage with seamless file management, secure sharing, and lightning-fast access to your digital world.'
    },
    {
      property: 'og:type',
      content: 'website'
    },
    {
      property: 'og:url',
      content: 'https://cms.antodono.com'
    },
    {
      property: 'og:image',
      content: '/logo.png'
    },
    {
      property: 'og:image:alt',
      content: 'ZhenCMS Logo'
    },
    {
      property: 'og:site_name',
      content: 'ZhenCMS'
    },
    // Twitter Card meta tags
    {
      name: 'twitter:card',
      content: 'summary_large_image'
    },
    {
      name: 'twitter:title',
      content: 'ZhenCMS - Modern Cloud Storage & File Management'
    },
    {
      name: 'twitter:description',
      content: 'Experience the future of cloud storage with seamless file management, secure sharing, and lightning-fast access to your digital world.'
    },
    {
      name: 'twitter:image',
      content: '/logo.png'
    },
    {
      name: 'twitter:image:alt',
      content: 'ZhenCMS Logo'
    },
    // Additional meta tags
    {
      name: 'theme-color',
      content: '#0ea5e9'
    },
    {
      name: 'application-name',
      content: 'ZhenCMS'
    },
    {
      name: 'apple-mobile-web-app-title',
      content: 'ZhenCMS'
    },
    {
      name: 'apple-mobile-web-app-capable',
      content: 'yes'
    },
    {
      name: 'apple-mobile-web-app-status-bar-style',
      content: 'default'
    }
  ],
  link: [
    {
      rel: 'icon',
      type: 'image/png',
      href: '/logo.png'
    },
    {
      rel: 'apple-touch-icon',
      href: '/logo.png'
    },
    {
      rel: 'canonical',
      href: 'https://cms.antodono.com'
    }
  ]
})
</script>

<style scoped>
/* Enhanced custom animations */
@keyframes blob {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  33% {
    transform: translate(30px, -50px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
  }
}

@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
  }
  50% {
    box-shadow: 0 0 40px rgba(59, 130, 246, 0.8);
  }
}

@keyframes gradient-x {
  0%, 100% {
    background-size: 200% 200%;
    background-position: left center;
  }
  50% {
    background-size: 200% 200%;
    background-position: right center;
  }
}

@keyframes spin-slow {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes expand {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}

@keyframes heartbeat {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
}

@keyframes typewriter {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

.animate-blob {
  animation: blob 8s infinite;
}

.animate-fade-in-up {
  animation: fade-in-up 1s ease-out forwards;
  opacity: 0;
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-pulse-glow {
  animation: pulse-glow 3s ease-in-out infinite;
}

.animate-gradient-x {
  animation: gradient-x 4s ease infinite;
}

.animate-spin-slow {
  animation: spin-slow 8s linear infinite;
}

.animate-expand {
  animation: expand 2s ease-out forwards;
  width: 0%;
}

.animate-heartbeat {
  animation: heartbeat 2s ease-in-out infinite;
}

.animate-typewriter {
  overflow: hidden;
  white-space: nowrap;
  animation: typewriter 3s steps(60, end) forwards;
  animation-delay: 1.5s;
  width: 0;
}

/* Animation delays */
.animation-delay-300 {
  animation-delay: 0.3s;
}

.animation-delay-500 {
  animation-delay: 0.5s;
}

.animation-delay-600 {
  animation-delay: 0.6s;
}

.animation-delay-900 {
  animation-delay: 0.9s;
}

.animation-delay-1000 {
  animation-delay: 1s;
}

.animation-delay-1200 {
  animation-delay: 1.2s;
}

.animation-delay-1500 {
  animation-delay: 1.5s;
}

.animation-delay-1800 {
  animation-delay: 1.8s;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-2100 {
  animation-delay: 2.1s;
}

.animation-delay-3000 {
  animation-delay: 3s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}
</style>
