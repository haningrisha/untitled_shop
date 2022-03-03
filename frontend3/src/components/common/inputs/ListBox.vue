<template>
    <Listbox as="div" v-model="selectedOption">
      <div class="relative">
        <ListboxButton
      class="relative list-box focus:outline-none focus-visible:ring-2 focus-visible:ring-opacity-75 focus-visible:ring-white focus-visible:ring-offset-orange-300 focus-visible:ring-offset-2 focus-visible:border-indigo-500 font-body border-2 text-tiny bg-gray-100 border-gray-900"
      v-slot="{ active }"
      >
        {{ selectedOption.name }}
        <span
            class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none"
          >
            <ChevronDownIcon v-if="!active" width="18" height="10" class="w-4 h-4 text-black" aria-hidden="true" />
            <ChevronUpIcon v-if="active" class="w-5 h-5 text-black" aria-hidden="true" />
          </span>
      </ListboxButton>

      <ListboxOptions class="absolute w-full z-10 border-2 border-t-0 border-black py-2 overflow-auto">
       <ListboxOption
         v-for="person in options"
         :key="person.name"
         :value="person"
         :disabled="false"
         as="template"
         v-slot="{active}"
        >
         <li :class="[active ? 'bg-gray-200' : 'bg-gray-100', 'relative']">
           <div class="flex justify-center font-body">
          {{ person.name }}
         </div>
         </li>
        </ListboxOption>
      </ListboxOptions>
      </div>
    </Listbox>
</template>

<script>
import {
  Listbox,
  ListboxButton,
  ListboxOption,
  ListboxOptions
} from '@headlessui/vue';
import {
    ChevronUpIcon
} from '@heroicons/vue/outline'
import ChevronDownIcon from "../../icons/ChevronDownIcon";
import {ref} from "vue";

export default {
  name: 'ListBox',
  props: {
    options: Object
  },
  components: {
    Listbox,
    ListboxButton,
    ListboxOption,
    ListboxOptions,
    ChevronDownIcon,
    ChevronUpIcon
  },
  data() {
    return {
      selectedOption: ref(this.options[0])
    }
  },
}
</script>

<style scoped>
  .list-box {
    @apply relative w-full py-2 pl-3 pr-10 text-left cursor-default justify-center flex;
  }
</style>