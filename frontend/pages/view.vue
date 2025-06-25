<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 via-sky-100 to-blue-200">
        <!-- Enhanced Navigation -->
        <nav class="bg-white/90 backdrop-blur-md shadow-lg border-b border-blue-100 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between items-center h-16">
                    <div class="flex items-center">
                        <NuxtLink to="/" class="flex items-center space-x-3 group">
                            <div class="w-10 h-10 group-hover:shadow-blue-500/25 transition-all duration-300 group-hover:scale-110">
                                <img src="~/assets/images/logo.png" alt="ZhenCMS Logo" class="w-full h-full object-contain rounded-xl" />
                            </div>
                            <span class="text-xl font-bold bg-gradient-to-r from-blue-600 to-sky-600 bg-clip-text text-transparent">ZhenCMS</span>
                        </NuxtLink>
                    </div>
                    <div class="flex items-center space-x-4">
                        <NuxtLink to="/" class="text-blue-600 hover:text-blue-800 transition-colors font-medium flex items-center space-x-2 group">
                            <svg class="w-4 h-4 group-hover:-translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                            </svg>
                            <span>Back to Home</span>
                        </NuxtLink>
                    </div>
                </div>
            </div>
        </nav>

        <!-- Main content -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <!-- Loading state -->
            <div v-if="loading" class="flex justify-center items-center py-20">
                <div class="relative">
                    <div class="animate-spin rounded-full h-16 w-16 border-4 border-blue-200"></div>
                    <div class="animate-spin rounded-full h-16 w-16 border-4 border-sky-500 border-t-transparent absolute top-0 left-0"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-6 h-6 bg-blue-500 rounded-full animate-pulse"></div>
                    </div>
                </div>
            </div>

            <!-- Error state -->
            <div v-else-if="error" class="text-center py-20">
                <div class="bg-gradient-to-br from-red-50 to-pink-50 border border-red-200 rounded-2xl p-8 max-w-md mx-auto shadow-xl">
                    <svg class="w-20 h-20 text-red-400 mx-auto mb-6 animate-bounce" fill="none" stroke="currentColor"
                        viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.464 0L4.35 16.5c-.77.833.192 2.5 1.732 2.5z">
                        </path>
                    </svg>
                    <h3 class="text-xl font-bold text-red-800 mb-3">{{ errorTitle }}</h3>
                    <p class="text-red-600 mb-6">{{ errorMessage }}</p>
                    <NuxtLink to="/"
                        class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-sky-600 text-white rounded-xl hover:from-blue-700 hover:to-sky-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg font-medium">
                        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
                        </svg>
                        Go Home
                    </NuxtLink>
                </div>
            </div>

            <!-- File content -->
            <div v-else-if="fileData" class="space-y-8 animate-fade-in-up">
                <!-- File info header -->
                <div class="bg-white/90 backdrop-blur-md rounded-2xl shadow-xl border border-blue-100 p-8 hover:shadow-2xl transition-all duration-500">
                    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
                        <div class="flex items-center space-x-6 mb-6 sm:mb-0">
                            <div
                                class="w-16 h-16 bg-gradient-to-br from-blue-100 via-sky-100 to-blue-200 rounded-2xl flex items-center justify-center shadow-lg">
                                <svg v-if="fileData.is_image" class="w-8 h-8 text-blue-600" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z">
                                    </path>
                                </svg>
                                <svg v-else-if="fileData.is_document" class="w-8 h-8 text-sky-600" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z">
                                    </path>
                                </svg>
                                <svg v-else class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z">
                                    </path>
                                </svg>
                            </div>
                            <div>
                                <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-800 to-sky-700 bg-clip-text text-transparent">{{ fileData.name }}</h1>
                                <div class="flex items-center space-x-4 text-sm text-blue-600 mt-2">
                                    <span class="px-2 py-1 bg-blue-100 rounded-full">{{ fileData.formatted_size }}</span>
                                    <span>•</span>
                                    <span class="px-2 py-1 bg-sky-100 rounded-full">{{ fileData.content_type.toUpperCase() }}</span>
                                    <span>•</span>
                                    <span>{{ formatDate(fileData.uploaded_at) }}</span>
                                </div>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <button @click="downloadFile"
                                class="group inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-sky-600 text-white rounded-xl hover:from-blue-700 hover:to-sky-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg font-medium">
                                <svg class="w-5 h-5 mr-2 group-hover:animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z">
                                    </path>
                                </svg>
                                Download
                            </button>
                            <button v-if="fileData.shareable" @click="copyShareLink"
                                class="group inline-flex items-center px-6 py-3 bg-gradient-to-r from-sky-100 to-blue-100 text-blue-700 rounded-xl hover:from-sky-200 hover:to-blue-200 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg font-medium border border-blue-200">
                                <svg class="w-5 h-5 mr-2 group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z">
                                    </path>
                                </svg>
                                {{ copied ? 'Copied!' : 'Share' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- File viewer -->
                <div class="bg-white/90 backdrop-blur-md rounded-2xl shadow-xl border border-blue-100 overflow-hidden hover:shadow-2xl transition-all duration-500">
                    <!-- Image viewer -->
                    <div v-if="fileData.is_image" class="p-8">
                        <div class="flex justify-center">
                            <img :src="getFileUrl(fileData.file_url)" :alt="fileData.name"
                                class="max-w-full h-auto rounded-xl shadow-2xl border border-blue-100 hover:scale-105 transition-transform duration-500" style="max-height: 70vh;" />
                        </div>
                    </div>

                    <!-- Document viewer (iframe for PDFs and other documents) -->
                    <div v-else-if="fileData.is_document || fileData.content_type === 'pdf'" class="relative">
                        <iframe :src="getFileUrl(fileData.file_url)" class="w-full border-0 rounded-b-2xl" style="height: 70vh;"
                            frameborder="0">
                            <p>Your browser does not support iframes. <a :href="getFileUrl(fileData.file_url)"
                                    target="_blank" class="text-blue-600 hover:text-blue-800">Click here to view the file</a>.</p>
                        </iframe>
                    </div>

                    <!-- Text file viewer (JSON, TXT, etc.) -->
                    <div v-else-if="isTextFile(fileData)" class="relative">
                        <!-- Loading state for text content -->
                        <div v-if="loadingTextContent" class="flex justify-center items-center py-20">
                            <div class="relative">
                                <div class="animate-spin rounded-full h-12 w-12 border-4 border-blue-200"></div>
                                <div class="animate-spin rounded-full h-12 w-12 border-4 border-sky-500 border-t-transparent absolute top-0 left-0"></div>
                            </div>
                            <span class="ml-4 text-blue-600 font-medium">Loading content...</span>
                        </div>

                        <!-- Text content error -->
                        <div v-else-if="textContentError" class="p-8 text-center">
                            <div class="w-20 h-20 bg-gradient-to-br from-red-100 to-pink-100 rounded-full flex items-center justify-center mx-auto mb-6 shadow-lg">
                                <svg class="w-10 h-10 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.464 0L4.35 16.5c-.77.833.192 2.5 1.732 2.5z">
                                    </path>
                                </svg>
                            </div>
                            <h3 class="text-xl font-bold text-red-800 mb-3">Cannot load content</h3>
                            <p class="text-red-600 mb-6">{{ textContentError }}</p>
                            <button @click="downloadFile"
                                class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-sky-600 text-white rounded-xl hover:from-blue-700 hover:to-sky-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg font-medium">
                                Download File
                            </button>
                        </div>

                        <!-- Text content display -->
                        <div v-else-if="textContent" class="relative">
                                                         <!-- Text viewer header -->
                             <div class="bg-gradient-to-r from-blue-50 to-sky-50 border-b border-blue-100 px-6 py-4">
                                 <div class="flex items-center justify-between mb-2">
                                     <div class="flex items-center space-x-3">
                                         <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                 d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z">
                                             </path>
                                         </svg>
                                         <h3 class="font-semibold text-blue-800">{{ getFileTypeLabel(fileData) }} Preview</h3>
                                     </div>
                                     <div class="flex items-center space-x-2">
                                         <button @click="copyTextContent"
                                             class="inline-flex items-center px-3 py-1.5 bg-blue-100 hover:bg-blue-200 text-blue-700 rounded-lg transition-colors duration-200 text-sm font-medium">
                                             <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                     d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z">
                                                 </path>
                                             </svg>
                                             {{ textCopied ? 'Copied!' : 'Copy' }}
                                         </button>
                                         <span class="text-sm text-blue-600">{{ formatFileSize(textContent.length) }} characters</span>
                                     </div>
                                 </div>
                                 
                                 <!-- Partial content warning -->
                                 <div v-if="isPartialContent" class="flex items-center space-x-2 text-sm text-amber-700 bg-amber-50 border border-amber-200 rounded-lg px-3 py-2">
                                     <svg class="w-4 h-4 text-amber-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                             d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.464 0L4.35 16.5c-.77.833.192 2.5 1.732 2.5z">
                                         </path>
                                     </svg>
                                     <span>
                                         Showing first {{ formatFileSize(textContent.length) }} of {{ fileData.formatted_size }} - 
                                         <button @click="downloadFile" class="underline hover:no-underline font-medium">
                                             download complete file
                                         </button>
                                     </span>
                                 </div>
                             </div>

                            <!-- Text content area -->
                            <div class="relative" style="height: 60vh;">
                                <pre class="h-full w-full p-6 overflow-auto text-sm font-mono bg-gradient-to-br from-gray-50 to-blue-50 text-gray-800 leading-relaxed whitespace-pre-wrap break-words border-0 resize-none focus:outline-none"><code :class="getLanguageClass(fileData)">{{ formattedTextContent }}</code></pre>
                            </div>
                        </div>
                    </div>

                    <!-- Generic file viewer -->
                    <div v-else class="p-16 text-center">
                        <div class="w-32 h-32 bg-gradient-to-br from-blue-100 to-sky-100 rounded-full flex items-center justify-center mx-auto mb-8 shadow-lg">
                            <svg class="w-16 h-16 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z">
                                </path>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-bold text-blue-800 mb-4">Preview not available</h3>
                        <p class="text-blue-600 mb-8 text-lg">This file type cannot be previewed in the browser.</p>
                        <button @click="downloadFile"
                            class="group inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-600 to-sky-600 text-white rounded-xl hover:from-blue-700 hover:to-sky-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg font-medium text-lg">
                            <svg class="w-6 h-6 mr-3 group-hover:animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z">
                                </path>
                            </svg>
                            Download to View
                        </button>
                    </div>
                </div>

                <!-- File details -->
                <div class="bg-white/90 backdrop-blur-md rounded-2xl shadow-xl border border-blue-100 p-8 hover:shadow-2xl transition-all duration-500">
                    <h3 class="text-2xl font-bold bg-gradient-to-r from-blue-800 to-sky-700 bg-clip-text text-transparent mb-6">File Details</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="space-y-6">
                            <div class="p-4 bg-gradient-to-r from-blue-50 to-sky-50 rounded-xl border border-blue-100">
                                <span class="text-sm font-semibold text-blue-600 uppercase tracking-wide">File Name</span>
                                <p class="text-blue-900 font-medium text-lg mt-1">{{ fileData.name }}{{ fileData.file_extension }}</p>
                            </div>
                            <div class="p-4 bg-gradient-to-r from-sky-50 to-blue-50 rounded-xl border border-sky-100">
                                <span class="text-sm font-semibold text-sky-600 uppercase tracking-wide">File Size</span>
                                <p class="text-sky-900 font-medium text-lg mt-1">{{ fileData.formatted_size }}</p>
                            </div>
                            <div class="p-4 bg-gradient-to-r from-blue-50 to-sky-50 rounded-xl border border-blue-100">
                                <span class="text-sm font-semibold text-blue-600 uppercase tracking-wide">Content Type</span>
                                <p class="text-blue-900 font-medium text-lg mt-1">{{ fileData.content_type }}</p>
                            </div>
                        </div>
                        <div class="space-y-6">
                            <div class="p-4 bg-gradient-to-r from-sky-50 to-blue-50 rounded-xl border border-sky-100">
                                <span class="text-sm font-semibold text-sky-600 uppercase tracking-wide">Upload Date</span>
                                <p class="text-sky-900 font-medium text-lg mt-1">{{ formatDate(fileData.uploaded_at) }}</p>
                            </div>
                            <div class="p-4 bg-gradient-to-r from-blue-50 to-sky-50 rounded-xl border border-blue-100">
                                <span class="text-sm font-semibold text-blue-600 uppercase tracking-wide">UUID</span>
                                <p class="text-blue-900 font-mono text-sm mt-1 break-all">{{ fileData.uuid }}</p>
                            </div>
                            <div class="p-4 bg-gradient-to-r from-sky-50 to-blue-50 rounded-xl border border-sky-100 flex items-center justify-start gap-2">
                                <span class="text-sm font-semibold text-sky-600 uppercase tracking-wide">Shareable</span>
                                <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold"
                                    :class="fileData.shareable ? 'bg-green-100 text-green-800 border border-green-200' : 'bg-red-100 text-red-800 border border-red-200'">
                                    {{ fileData.shareable ? 'Yes' : 'No' }}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Enhanced Toast notification -->
        <div v-if="showToast"
            class="fixed top-6 right-6 bg-gradient-to-r from-green-500 to-emerald-600 text-white px-8 py-4 rounded-2xl shadow-2xl transform transition-all duration-500 z-50 animate-slide-in-right">
            <div class="flex items-center">
                <svg class="w-6 h-6 mr-3 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                <span class="font-medium">
                    {{ isPartialContent && textCopied ? 'Partial content copied to clipboard!' : 'Link copied to clipboard!' }}
                </span>
            </div>
        </div>
    </div>
</template>

<script setup>
const route = useRoute()
const config = useRuntimeConfig()

// Reactive data
const loading = ref(true)
const error = ref(false)
const errorTitle = ref('')
const errorMessage = ref('')
const fileData = ref(null)
const copied = ref(false)
const showToast = ref(false)

// Text file preview data
const textContent = ref('')
const loadingTextContent = ref(false)
const textContentError = ref('')
const textCopied = ref(false)
const isPartialContent = ref(false)

// Get file ID from query params
const fileId = computed(() => route.query.id)

// Fetch file data on mount
onMounted(async () => {
    if (!fileId.value) {
        setError('Missing File ID', 'No file ID provided in the URL.')
        return
    }

    await fetchFileData()
})

// Watch for route changes
watch(() => route.query.id, async (newId) => {
    if (newId && newId !== fileId.value) {
        loading.value = true
        error.value = false
        await fetchFileData()
    }
})

async function fetchFileData() {
    try {
        loading.value = true
        error.value = false

        const response = await $fetch(`${config.public.apiBase}/file/api/get-by-uuid/`, {
            method: 'POST',
            body: {
                uuid: fileId.value
            }
        })

        fileData.value = response

        // If it's a text file, fetch the content
        if (isTextFile(response)) {
            await fetchTextContent()
        }
    } catch (err) {
        console.error('Error fetching file:', err)

        if (err.status === 403) {
            setError('Access Forbidden', 'You do not have permission to view this file.')
        } else if (err.status === 404) {
            setError('File Not Found', 'The requested file could not be found.')
        } else {
            setError('Error Loading File', 'An unexpected error occurred while loading the file.')
        }
    } finally {
        loading.value = false
    }
}

function setError(title, message) {
    error.value = true
    errorTitle.value = title
    errorMessage.value = message
    loading.value = false
}

function getFileUrl(filePath) {
    return `${config.public.apiBase}${filePath}`
}

function downloadFile() {
    if (!fileData.value) return

    const link = document.createElement('a')
    link.href = getFileUrl(fileData.value.file_url)
    link.download = `${fileData.value.name}${fileData.value.file_extension}`
    link.target = '_blank'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
}

async function copyShareLink() {
    try {
        const currentUrl = window.location.href
        await navigator.clipboard.writeText(currentUrl)
        copied.value = true
        showToast.value = true

        setTimeout(() => {
            copied.value = false
        }, 2000)

        setTimeout(() => {
            showToast.value = false
        }, 3000)
    } catch (err) {
        console.error('Failed to copy link:', err)
    }
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}

// Text file handling functions
function isTextFile(file) {
    if (!file) return false
    
    const textExtensions = ['.txt', '.json', '.js', '.ts', '.html', '.css', '.xml', '.csv', '.md', '.py', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go', '.rs', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf', '.log', '.sql', '.sh', '.bat', '.ps1']
    const textContentTypes = ['text/', 'application/json', 'application/javascript', 'application/xml', 'application/csv']
    
    // Check by file extension
    if (file.file_extension && textExtensions.includes(file.file_extension.toLowerCase())) {
        return true
    }
    
    // Check by content type
    if (file.content_type) {
        return textContentTypes.some(type => file.content_type.toLowerCase().startsWith(type))
    }
    
    return false
}

async function fetchTextContent() {
    if (!fileData.value || !isTextFile(fileData.value)) return
    
    try {
        loadingTextContent.value = true
        textContentError.value = ''
        
        const response = await fetch(getFileUrl(fileData.value.file_url))
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        
        // For large files (>1MB), only load the first 500KB
        const maxPreviewSize = 500 * 1024 // 500KB
        const isLargeFile = fileData.value.size_in_bytes > 1024 * 1024 // 1MB
        
        if (isLargeFile) {
            // Use range request to get only the first part of the file
            const partialResponse = await fetch(getFileUrl(fileData.value.file_url), {
                headers: {
                    'Range': `bytes=0-${maxPreviewSize - 1}`
                }
            })
            
            if (partialResponse.ok || partialResponse.status === 206) {
                const text = await partialResponse.text()
                textContent.value = text
                isPartialContent.value = true
                return
            }
        }
        
        // For smaller files or if range request fails, load the entire file
        const text = await response.text()
        
        // If the full content is too large for display, truncate it
        if (text.length > maxPreviewSize) {
            textContent.value = text.substring(0, maxPreviewSize)
            isPartialContent.value = true
        } else {
            textContent.value = text
            isPartialContent.value = false
        }
        
    } catch (err) {
        console.error('Error fetching text content:', err)
        textContentError.value = 'Failed to load file content. The file might be corrupted or inaccessible.'
    } finally {
        loadingTextContent.value = false
    }
}

function getFileTypeLabel(file) {
    if (!file) return 'File'
    
    const ext = file.file_extension?.toLowerCase()
    switch (ext) {
        case '.json': return 'JSON'
        case '.js': return 'JavaScript'
        case '.ts': return 'TypeScript'
        case '.html': return 'HTML'
        case '.css': return 'CSS'
        case '.xml': return 'XML'
        case '.csv': return 'CSV'
        case '.md': return 'Markdown'
        case '.py': return 'Python'
        case '.java': return 'Java'
        case '.cpp': case '.cc': case '.cxx': return 'C++'
        case '.c': return 'C'
        case '.h': return 'Header'
        case '.php': return 'PHP'
        case '.rb': return 'Ruby'
        case '.go': return 'Go'
        case '.rs': return 'Rust'
        case '.yaml': case '.yml': return 'YAML'
        case '.toml': return 'TOML'
        case '.ini': case '.cfg': case '.conf': return 'Configuration'
        case '.log': return 'Log'
        case '.sql': return 'SQL'
        case '.sh': return 'Shell Script'
        case '.bat': return 'Batch'
        case '.ps1': return 'PowerShell'
        case '.txt': return 'Text'
        default: return 'Text'
    }
}

function getLanguageClass(file) {
    if (!file) return ''
    
    const ext = file.file_extension?.toLowerCase()
    switch (ext) {
        case '.json': return 'language-json'
        case '.js': return 'language-javascript'
        case '.ts': return 'language-typescript'
        case '.html': return 'language-html'
        case '.css': return 'language-css'
        case '.xml': return 'language-xml'
        case '.md': return 'language-markdown'
        case '.py': return 'language-python'
        case '.java': return 'language-java'
        case '.cpp': case '.cc': case '.cxx': return 'language-cpp'
        case '.c': return 'language-c'
        case '.php': return 'language-php'
        case '.rb': return 'language-ruby'
        case '.go': return 'language-go'
        case '.rs': return 'language-rust'
        case '.yaml': case '.yml': return 'language-yaml'
        case '.sql': return 'language-sql'
        case '.sh': return 'language-bash'
        default: return 'language-text'
    }
}

const formattedTextContent = computed(() => {
    if (!textContent.value) return ''
    
    // For JSON files, try to format them nicely
    if (fileData.value?.file_extension?.toLowerCase() === '.json') {
        try {
            const parsed = JSON.parse(textContent.value)
            return JSON.stringify(parsed, null, 2)
        } catch (e) {
            // If it's not valid JSON, just return as-is
            return textContent.value
        }
    }
    
    return textContent.value
})

async function copyTextContent() {
    if (!textContent.value) return
    
    try {
        await navigator.clipboard.writeText(textContent.value)
        textCopied.value = true
        
        // Show different message for partial content
        if (isPartialContent.value) {
            showToast.value = true
            setTimeout(() => {
                showToast.value = false
            }, 3000)
        }
        
        setTimeout(() => {
            textCopied.value = false
        }, 2000)
    } catch (err) {
        console.error('Failed to copy text content:', err)
    }
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 B'
    
    const k = 1024
    const sizes = ['B', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
}

// SEO and meta data for better embeds
useHead({
    title: computed(() => {
        if (fileData.value) {
            return `${fileData.value.name} - ZhenCMS`
        }
        return 'View File - ZhenCMS'
    }),
    meta: [
        {
            name: 'description',
            content: computed(() => {
                if (fileData.value) {
                    return `View and download ${fileData.value.name} (${fileData.value.formatted_size}) - Secure cloud storage with ZhenCMS`
                }
                return 'View and download files securely with ZhenCMS - Modern cloud storage platform'
            })
        },
        {
            name: 'keywords',
            content: 'file sharing, cloud storage, download, view files, ZhenCMS, secure storage'
        },
        {
            name: 'author',
            content: 'Youwei Zhen'
        },
        // Open Graph meta tags for better social media embeds
        {
            property: 'og:title',
            content: computed(() => {
                if (fileData.value) {
                    return `${fileData.value.name} - ZhenCMS`
                }
                return 'View File - ZhenCMS'
            })
        },
        {
            property: 'og:description',
            content: computed(() => {
                if (fileData.value) {
                    return `View and download ${fileData.value.name} (${fileData.value.formatted_size}) - Secure cloud storage with ZhenCMS`
                }
                return 'View and download files securely with ZhenCMS - Modern cloud storage platform'
            })
        },
        {
            property: 'og:type',
            content: 'website'
        },
        {
            property: 'og:image',
            content: computed(() => {
                if (fileData.value && fileData.value.is_image) {
                    return getFileUrl(fileData.value.file_url)
                }
                return '/logo.png'
            })
        },
        {
            property: 'og:image:alt',
            content: computed(() => {
                if (fileData.value && fileData.value.is_image) {
                    return fileData.value.name
                }
                return 'ZhenCMS Logo'
            })
        },
        {
            property: 'og:site_name',
            content: 'ZhenCMS'
        },
        // Twitter Card meta tags
        {
            name: 'twitter:card',
            content: computed(() => {
                if (fileData.value && fileData.value.is_image) {
                    return 'summary_large_image'
                }
                return 'summary'
            })
        },
        {
            name: 'twitter:title',
            content: computed(() => {
                if (fileData.value) {
                    return `${fileData.value.name} - ZhenCMS`
                }
                return 'View File - ZhenCMS'
            })
        },
        {
            name: 'twitter:description',
            content: computed(() => {
                if (fileData.value) {
                    return `View and download ${fileData.value.name} (${fileData.value.formatted_size}) - Secure cloud storage with ZhenCMS`
                }
                return 'View and download files securely with ZhenCMS - Modern cloud storage platform'
            })
        },
        {
            name: 'twitter:image',
            content: computed(() => {
                if (fileData.value && fileData.value.is_image) {
                    return getFileUrl(fileData.value.file_url)
                }
                return '/logo.png'
            })
        },
        {
            name: 'twitter:image:alt',
            content: computed(() => {
                if (fileData.value && fileData.value.is_image) {
                    return fileData.value.name
                }
                return 'ZhenCMS Logo'
            })
        },
        // Additional meta tags
        {
            name: 'theme-color',
            content: '#0ea5e9'
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
        }
    ]
})
</script>

<style scoped>
/* Enhanced animations */
@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slide-in-right {
    from {
        opacity: 0;
        transform: translateX(100%);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes pulse-blue {
    0%, 100% {
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
    }
    50% {
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.6);
    }
}

.animate-fade-in-up {
    animation: fade-in-up 0.8s ease-out forwards;
}

.animate-slide-in-right {
    animation: slide-in-right 0.5s ease-out forwards;
}

.animate-pulse-blue {
    animation: pulse-blue 2s ease-in-out infinite;
}

/* Hover effects */
.hover\:scale-105:hover {
    transform: scale(1.05);
}

/* Backdrop blur fallback */
@supports not (backdrop-filter: blur(12px)) {
    .backdrop-blur-md {
        background-color: rgba(255, 255, 255, 0.95);
    }
}
</style>