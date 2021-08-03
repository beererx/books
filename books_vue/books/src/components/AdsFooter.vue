<template>
    <b-container>
        <div>
            <a :href="rowAdsData.data.url" target="_blank">
                <img style="width:100%" :src="rowAdsData.data.img_path" :alt="rowAdsData.data.alt" />
            </a>
            </div>
    </b-container>
</template>

<script>
export default {
  name: "AdsFooter",
  setup(props,context){
      return{

      }
  }
};
</script>

<style scoped lang="scss">

</style>
