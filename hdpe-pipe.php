<?php 
$current_page = basename($_SERVER['PHP_SELF']);
$page_titles = [
	'hdpe-pipe.php' => 'HDPE PIPE',
	'hdpe-roll-pipe.php' => 'HDPE ROLL PIPE',
	'sprinkler-pipe.php' => 'SPRINKLER PIPE',
	'sprinkler-fitting.php' => 'SPRINKLER FITTING',
	'mdpe-pipe.php' => 'MDPE PIPE',
	'rubber-washer.php' => 'RUBBER WASHER'
];
$title = isset($page_titles[$current_page]) ? $page_titles[$current_page] : 'Water Supply Scheme';
include 'header.php'; 
?>
<div class="tstk-title-bar-wrapper  tstk-bg-color-secondarycolor tstk-bg-image-yes tstk-titlebar-style-left">
		<div class="container">
			<div class="tstk-title-bar-content">
				<div class="tstk-title-bar-content-inner">
					<div class="tstk-tbar"><div class="tstk-tbar-inner container"><h1 class="tstk-tbar-title"> <?php echo $title; ?></h1><h3 class="tstk-tbar-subtitle"> Product</h3></div></div>					<div class="tstk-breadcrumb"><div class="tstk-breadcrumb-inner"><span><a title="Go to Home." href="index.php" class="home"><span>Home</span></a></span><span class="sep"><i class="tstk-base-icon-angle-double-right"></i></span><span><span class="post post-tstk-service current-item"><?php echo $title; ?></span></span></div></div>
				</div>
			</div><!-- .tstk-title-bar-content -->
		</div><!-- .container -->
	</div><!-- .tstk-title-bar-wrapper -->
      <div class="site-content-contain ">
        <div class="site-content-wrap">
          <div id="content" class="site-content container">
            <div class="row multi-columns-row">
              <div class="tstk-header-search-form-wrapper">
                <div class="tstk-search-close"><i class="tstk-base-icon-cancel"></i></div>
                <form role="search" method="get" class="search-form" action="">
                  <label for="search-form-6a1837587ca7d">
                  <span class="screen-reader-text">Search for:</span>
                  </label>
                  <input type="search" id="search-form-6a1837587ca7d" class="search-field" placeholder="Search &hellip;" value="" name="s" />
                  <button type="submit" title="Search" class="search-submit"><span class="screen-reader-text">Search</span></button>
                </form>
              </div>
              <div id="primary" class="content-area col-md-9 col-lg-9">
                <main id="main" class="site-main">
                  <article id="post-7558" class="tstk-service-single-style-1 post-7558 tstk-service type-tstk-service status-publish has-post-thumbnail hentry tstk-service-category-chemical">
                    <div class="tstk-service-single">
                      <div class="tstk-service-feature-image">
                        <div class="tstk-featured-wrapper"><img fetchpriority="high" width="1200" height="1000" src="images/brands/HDPE PIPE.png" class="img-fluid w-100 mb-4" alt="HDPE PIPE" /></div>
                      </div>
                      <div class="tstk-entry-content">
                        <div class="product-details-content mb-5 mt-4">
        <h2>HDPE PIPE</h2>
        <div class="elementor-widget-container">
            <p>HDPE pipe is known for its high strength to density ratio. HDPE has little branching giving it stronger intermolecular forces and tensile strength than HDPE and more opaque and can withstand somewhat higher temperature.</p>
            <table class="table table-bordered table-striped mt-4">
                <tbody>
                    <tr><th>Size (MM)</th><td>20MM to 160MM</td></tr>
                    <tr><th>Material</th><td>GradePE63, PE80, PE100</td></tr>
                    <tr><th>Working Pressure</th><td>2.5kgf/cm2 to 20kgf/cm2</td></tr>
                    <tr><th>SDR</th><td>SDR41 to SDR6</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <!-- .entry-content -->
                      <nav class="navigation post-navigation" aria-label="Posts">
                        <h2 class="screen-reader-text">Post navigation</h2>
                        <div class="nav-links">
                          <div class="nav-previous"><a href="../machine-learning-analysis/index.html" rel="prev"><span class="tstk-service-nav-icon"><i class="tstk-base-icon-left-open"></i></span> <span class="tstk-service-nav-wrapper"><span class="tstk-service-nav-head">Previous Service</span><span class="tstk-service-nav nav-title">Machine learning Analysis</span> </span></a></div>
                          <div class="nav-next"><a href="../maintenance-and-repairing/index.html" rel="next"><span class="tstk-service-nav-wrapper"><span class="tstk-service-nav-head">Next Service</span><span class="tstk-service-nav nav-title">Maintenance and Repairing</span> </span> <span class="tstk-service-nav-icon"><i class="tstk-base-icon-right-open"></i></span></a></div>
                        </div>
                      </nav>
                    </div>
                  </article>
                  <!-- #post-## -->
                </main>
                <!-- #main -->
              </div>
              <!-- #primary -->
              <aside id="secondary" class="widget-area themestek-sidebar col-md-3 col-lg-3" aria-label="Service Sidebar">
                <aside id="tstk-list-all-posts-1" class="widget-odd widget-19 widget tstk_widget_list_all_posts industrey_widget  industrey_widget_count_19">
                  <h2 class="widget-title">Products</h2>
                  <div class="tstk-all-post-list-w">
                    <ul class="tstk-all-post-list">
                      <?php 
                      $services = [
                        'hdpe-pipe.php' => 'HDPE PIPE',
                        'hdpe-roll-pipe.php' => 'HDPE ROLL PIPE',
                        'sprinkler-pipe.php' => 'SPRINKLER PIPE',
                        'sprinkler-fitting.php' => 'SPRINKLER FITTING',
                        'mdpe-pipe.php' => 'MDPE PIPE',
                        'rubber-washer.php' => 'RUBBER WASHER'
                      ];
                      $current_file = basename($_SERVER['PHP_SELF']);
                      foreach ($services as $file => $name) {
                        $active = ($current_file == $file) ? 'tstk-post-active' : '';
                        echo '<li class="' . $active . '"><a href="' . $file . '"> ' . $name . ' </a></li>';
                      }
                      ?>
                    </ul>
                  </div>
                </aside>
                <aside id="custom_html-2" class="widget_text widget-even widget-20 tstk-download-file widget widget_custom_html industrey_widget  industrey_widget_count_20">
                  <div class="textwidget custom-html-widget">
                    <div class="download">
                      <div class="item-download"> 
                        <a href="images/Sethi Pipe Brochure.pdf" target="_blank" rel="noopener noreferrer"><i class="industrey-base-icons tstk-base-icon-pdf"></i> Download our Brochures <i class="industrey-base-icons tstk-rightpostn tstk-base-icon-download"></i></a>
                      </div>
                      <div class="item-download">
                        <a href="images/Sethi Pipe company Brochure.pdf" target="_blank" rel="noopener noreferrer"><i class="industrey-base-icons  tstk-base-icon-doc-text-inv"></i>  Our company details  <i class="industrey-base-icons tstk-rightpostn tstk-base-icon-download"></i></a>
                      </div>
                    </div>
                  </div>
                </aside>
                <aside id="custom_html-3" class="widget_text widget-odd widget-21 single-service-contact widget widget_custom_html industrey_widget  industrey_widget_count_21">
                  <div class="textwidget custom-html-widget">
                    <div class="single-service-contact-inner">
                      <h5>For a investor Inquiry</h5>
                      <p><img loading="lazy" class="size-full wp-image-28211 aligncenter" style="background-color: #fff;" src="images/SPLogo.png" alt="" width="100" height="100"></p>
                      <h5 class="tstk-service-title">Sethi Pipe</h5>
                      <p class="tstk-service-position">Shri Krishna Rubber Industries</p>
                      <ul>
                        <li style="list-style-type: none;">
                          <ul>
                            <li><i class="tstk-base-icon-phone-volume-solid"></i> +91 9425151151</li>
                            <li><i class="tstk-base-icon-mail-alt"></i> <a href="" class="__cf_email__" data-cfemail="0d606c64614d68756c607d6168236e6260">[email&#160;protected]</a></li>
                          </ul>
                        </li>
                      </ul>
                      <div role="form" class="wpcf7" id="wpcf7-f4-o7" lang="en-US" dir="ltr">
                        <div class="screen-reader-response">
                          <p role="status" aria-live="polite" aria-atomic="true"></p>
                          <ul></ul>
                        </div>
                        <form action="" method="post" class="wpcf7-form init" novalidate="novalidate" data-status="init">
                          <div style="display: none;">
                            <input type="hidden" name="_wpcf7" value="4">
                            <input type="hidden" name="_wpcf7_version" value="5.4.1">
                            <input type="hidden" name="_wpcf7_locale" value="en_US">
                            <input type="hidden" name="_wpcf7_unit_tag" value="wpcf7-f4-o7">
                            <input type="hidden" name="_wpcf7_container_post" value="0">
                            <input type="hidden" name="_wpcf7_posted_data_hash" value="">
                          </div>
                          <div class="main-form tstk-form-style-3">
                            <div class="row">
                              <div class="col-sm-12">
                                <div class="input-group"><span class="wpcf7-form-control-wrap your-email"><input type="email" name="your-email" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email" aria-required="true" aria-invalid="false" placeholder="Your Email Address.."></span></div>
                              </div>
                              <div class="col-sm-12">
                                <div class="input-group input-button">
                                  <button id="submit" class="wpcf7-form-control wpcf7-submit"><span>Send Your Request</span></button><span class="ajax-loader"></span>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="wpcf7-response-output" aria-hidden="true"></div>
                        </form>
                      </div>
                    </div>
                  </div>
                </aside>
              </aside>
              <!-- #secondary -->
            </div>
            <!-- .row -->
          </div>
          <!-- #content -->
        </div>
        <!-- .site-content-wrap -->
        <?php include 'footer.php'; ?>