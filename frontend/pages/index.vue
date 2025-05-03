<template>
  <div class="max-w-3xl mx-auto p-4 space-y-4">
    <div
        v-for="(email, index) in emails"
        :key="index"
        class="border rounded-lg shadow-sm p-4 transition-all duration-300 hover:shadow-md bg-white"
    >
      <div class="flex items-center justify-between cursor-pointer" @click="toggleExpand(index)">
        <p class="text-gray-800 font-medium">Email #{{ index + 1 }}</p>
        <div class="flex items-center space-x-2">
          <span v-if="email.response.is_phishing" class="text-red-500 font-semibold text-sm">⚠️ Phishing</span>
          <span v-else class="text-green-500 font-semibold text-sm">✔️ Safe</span>
        </div>
      </div>

      <div v-if="email.expanded" class="mt-4 border-t pt-4 space-y-2">
        <div v-html="email.mail" class="prose max-w-none text-gray-700"></div>
        <div v-if="email.response.is_phishing" class="mt-2 p-2 bg-red-50 border border-red-300 rounded">
          <p class="text-sm text-red-700 font-medium">Phishing Reason:</p>
          <p class="text-sm text-red-600">{{ email.response.reason }}</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface EmailResponse {
  is_phishing: boolean
  reason: string
}

interface EmailItem {
  mail: string
  response: EmailResponse
  expanded?: boolean // For toggling the dropdown
}

const emails = ref<EmailItem[]>([])

const fetchMails = async () => {
  const data = await $fetch<EmailItem[]>('http://127.0.0.1:8000/api/google/messages', {
    method: 'GET',
    credentials: 'include'
  })

  emails.value = data.map(item => ({ ...item, expanded: false }))
}

const toggleExpand = (index: number) => {
  emails.value[index].expanded = !emails.value[index].expanded
}

onMounted(() => {
  fetchMails()
})
</script>

