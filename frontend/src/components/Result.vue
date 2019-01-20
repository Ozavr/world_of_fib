<template>
    <div> 
        <md-card-header>
            <div class="md-title">Result</div>
        </md-card-header>

        <md-card-content id='result__text'>
            {{ result }}
        </md-card-content>
    </div> 
</template>

<script>
export default {
    props: {
        result: String
    },
    name: 'result'
}
</script>

<style>

</style>
