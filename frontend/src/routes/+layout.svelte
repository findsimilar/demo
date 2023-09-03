<script>
	import Header from './Header.svelte';
	import logo from '$lib/images/logo.png';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

    <footer class="footer mt-auto d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="index.html" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
        <img src="{logo}" class="bi" width="30" height="24" alt="FindSimilar logo">
      </a>
      <span class="mb-3 mb-md-0 text-muted">Copyleft &#127279; FindSimilar 2023</span>
    </div>

        <ul class="nav col-md-4 justify-content-end">
            <li class="nav-item"><a class="nav-link px-2 text-muted" target="_blank" href="https://github.com/findsimilar/demo"><i class="bi bi-github"></i></a></li>
    </ul>

  </footer>

</div>

