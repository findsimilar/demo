<script>
	import logo from '$lib/images/logo.png';
	import { Button } from 'sveltestrap';
</script>

<svelte:head>
	<title>demo.findsimilar.org</title>
	<meta name="description" content="FindSimilar demo app" />
</svelte:head>

<div class="text-center bg-body-tertiary rounded-3">
    <img src="{logo}" class="bi mt-4 mb-3" width="100" height="100">
    <h1 class="text-body-emphasis">Welcome to FindSimilar Demo Project!</h1>
    <p class="col-lg-8 mx-auto fs-5 text-muted">
      You can check the main features here.
    </p>
    <div class="d-inline-flex gap-2 mb-5">
        <a class="d-inline-flex align-items-center btn btn-primary btn-lg px-4 rounded-pill" href="/simple">Simple usage</a>
    </div>
</div>

