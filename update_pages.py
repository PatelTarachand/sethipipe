import re

pages = {
    'hdpe-pipe.php': {
        'title': 'HDPE PIPE',
        'image': 'images/brands/HDPE PIPE.png',
        'content': '''<div class="elementor-widget-container">
            <p>HDPE pipe is known for its high strength to density ratio. HDPE has little branching giving it stronger intermolecular forces and tensile strength than HDPE and more opaque and can withstand somewhat higher temperature.</p>
            <table class="table table-bordered table-striped mt-4">
                <tbody>
                    <tr><th>Size (MM)</th><td>20MM to 160MM</td></tr>
                    <tr><th>Material</th><td>GradePE63, PE80, PE100</td></tr>
                    <tr><th>Working Pressure</th><td>2.5kgf/cm2 to 20kgf/cm2</td></tr>
                    <tr><th>SDR</th><td>SDR41 to SDR6</td></tr>
                </tbody>
            </table>
        </div>'''
    },
    'hdpe-roll-pipe.php': {
        'title': 'HDPE ROLL PIPE',
        'image': 'images/brands/HDPE ROLL PIPE.png',
        'content': '''<div class="elementor-widget-container">
            <p>We are enlisted amongst the leading organization in the industry, offering a quality approved range of HDPE Roll Pipe that is delivered in various sizes and dimensions. The entire product range is manufactured with utmost accuracy. Owing to its durable standards and quality.</p>
            <p><strong>Customized Size Available</strong></p>
        </div>'''
    },
    'sprinkler-pipe.php': {
        'title': 'SPRINKLER PIPE',
        'image': 'images/brands/SPRINKLER PIPE.png',
        'content': '''<div class="elementor-widget-container">
            <p>We are an eminent manufacturer and supplier of a wide collection of HDPE sprinkler pipes. The offered pipes are fabricated using fine quality raw material. These HDPE sprinkler pipes are manufactured by using the finest of the raw material.</p>
            <ul class="tstk-list tstk-list-style-icon tstk-list-icon-color-skincolor">
                <li><i class="tstk-base-icon-right-open"></i> <strong>SIZE :</strong> 63mm, 75mm, 90mm, 110mm</li>
                <li><i class="tstk-base-icon-right-open"></i> <strong>Pressure :</strong> 2.5kgf/cm – 3.2kgf/cm</li>
            </ul>
        </div>'''
    },
    'mdpe-pipe.php': {
        'title': 'MDPE PIPE',
        'image': 'images/brands/MDPE PIPE.png',
        'content': '''<div class="elementor-widget-container">
            <p>MDPE (Medium Density Polyethylene) pipes are durable, flexible, and corrosion-resistant plastic pipes widely used for underground water mains and potable drinking water supply. Thanks to their lightweight, non-toxic nature, and resistance to environmental stress, they have become a standard, long-lasting alternative to traditional copper or galvanized steel plumbing.</p>
            
            <h4 class="mt-5 mb-3">Types of Adapters</h4>
            <div class="row text-center mb-4">
                <div class="col-md-4 mb-4"><img src="images/brands/Adapter HM Type.png" alt="Adapter HM Type" class="img-fluid"><br>Adapter HM Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Adapter C Type.png" alt="Adapter C Type" class="img-fluid"><br>Adapter C Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Adapter Bush HM Type.png" alt="Adapter Bush HM Type" class="img-fluid"><br>Adapter Bush HM Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Adapter Bush C Type.png" alt="Adapter Bush C Type" class="img-fluid"><br>Adapter Bush C Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/PCR C Type.png" alt="PCR C Type" class="img-fluid"><br>PCR C Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Bend C Type.png" alt="Bend C Type" class="img-fluid"><br>Bend C Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Coupler C type.png" alt="Coupler C type" class="img-fluid"><br>Coupler C type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Tee C Type.png" alt="Tee C Type" class="img-fluid"><br>Tee C Type</div>
                <div class="col-md-4 mb-4"><img src="images/brands/Y Type.png" alt="Y Type" class="img-fluid"><br>Y Type</div>
            </div>

            <h4 class="mt-4 mb-3">FEATURES & CHARACTERISTICS</h4>
            <div class="row">
                <div class="col-md-6">
                    <ul class="tstk-list tstk-list-style-icon tstk-list-icon-color-skincolor">
                        <li><i class="tstk-base-icon-right-open"></i> Corrosion-Resistant</li>
                        <li><i class="tstk-base-icon-right-open"></i> Light Weight & Flexible</li>
                        <li><i class="tstk-base-icon-right-open"></i> impact resistant & Tough, Durable</li>
                        <li><i class="tstk-base-icon-right-open"></i> Smooth Surface-low Pipe Friction Losses</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <ul class="tstk-list tstk-list-style-icon tstk-list-icon-color-skincolor">
                        <li><i class="tstk-base-icon-right-open"></i> Long Service Life</li>
                        <li><i class="tstk-base-icon-right-open"></i> Low Electrical Conductivity</li>
                        <li><i class="tstk-base-icon-right-open"></i> Environmental Friendly</li>
                        <li><i class="tstk-base-icon-right-open"></i> Good Weldability</li>
                    </ul>
                </div>
            </div>
        </div>'''
    },
    'rubber-washer.php': {
        'title': 'RUBBER WASHER',
        'image': 'wp-content/uploads/sites/5/2021/09/service-new-08.jpg',
        'content': '''<div class="elementor-widget-container">
            <div class="row text-center mb-5 mt-4">
                <div class="col-md-3"><img src="images/brands/Round Flange Washer.png" alt="Round Flange Washer" class="img-fluid"><br>Round Flange Washer</div>
                <div class="col-md-3"><img src="images/brands/Square Flange Washer.png" alt="Square Flange Washer" class="img-fluid"><br>Square Flange Washer</div>
                <div class="col-md-3"><img src="images/brands/Sprinkler Pipe Ring.png" alt="Sprinkler Pipe Ring" class="img-fluid"><br>Sprinkler Pipe Ring</div>
                <div class="col-md-3"><img src="images/brands/Tyton Gasket.png" alt="Tyton Gasket" class="img-fluid"><br>Tyton Gasket</div>
            </div>

            <h4 class="mt-4 mb-3">FEATURES & CHARACTERISTICS</h4>
            <div class="row">
                <div class="col-md-6">
                    <ul class="tstk-list tstk-list-style-icon tstk-list-icon-color-skincolor">
                        <li><i class="tstk-base-icon-right-open"></i> Corrosion-Resistant</li>
                        <li><i class="tstk-base-icon-right-open"></i> Light Weight & Flexible</li>
                        <li><i class="tstk-base-icon-right-open"></i> impact resistant & Tough, Durable</li>
                        <li><i class="tstk-base-icon-right-open"></i> Smooth Surface-low Pipe Friction Losses</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <ul class="tstk-list tstk-list-style-icon tstk-list-icon-color-skincolor">
                        <li><i class="tstk-base-icon-right-open"></i> Long Service Life</li>
                        <li><i class="tstk-base-icon-right-open"></i> Low Electrical Conductivity</li>
                        <li><i class="tstk-base-icon-right-open"></i> Environmental Friendly</li>
                        <li><i class="tstk-base-icon-right-open"></i> Good Weldability</li>
                    </ul>
                </div>
            </div>
        </div>'''
    }
}

new_title_array = """$page_titles = [
	'hdpe-pipe.php' => 'HDPE PIPE',
	'hdpe-roll-pipe.php' => 'HDPE ROLL PIPE',
	'sprinkler-pipe.php' => 'SPRINKLER PIPE',
	'mdpe-pipe.php' => 'MDPE PIPE',
	'rubber-washer.php' => 'RUBBER WASHER'
];"""

new_sidebar_array = """$services = [
                        'hdpe-pipe.php' => 'HDPE PIPE',
                        'hdpe-roll-pipe.php' => 'HDPE ROLL PIPE',
                        'sprinkler-pipe.php' => 'SPRINKLER PIPE',
                        'mdpe-pipe.php' => 'MDPE PIPE',
                        'rubber-washer.php' => 'RUBBER WASHER'
                      ];"""

for filename, data in pages.items():
    with open(f"/opt/lampp/htdocs/Sethipipe/{filename}", "r") as f:
        content = f.read()

    # 1. Replace the $page_titles array
    content = re.sub(
        r'\$page_titles = \[\s*\'water-supply.*?\];',
        new_title_array,
        content,
        flags=re.DOTALL
    )

    # 2. Replace the $services array in the sidebar
    content = re.sub(
        r'\$services = \[\s*\'water-supply.*?\];',
        new_sidebar_array,
        content,
        flags=re.DOTALL
    )

    # 3. Replace the main featured image
    content = re.sub(
        r'src="wp-content/uploads/sites/5/2021/09/service-new-08\.jpg"[^>]*>',
        f'src="{data["image"]}" class="img-fluid w-100 mb-4" alt="{data["title"]}" />',
        content
    )

    # 4. Remove all the Elementor content inside `<div class="tstk-entry-content">` up to the navigation nav element,
    # and replace with our simple static HTML.
    
    # Let's find the start of the elementor content and replace everything until </nav>
    # Wait, there's `<div data-elementor-type="wp-post" data-elementor-id="7558"` inside `<div class="tstk-entry-content">`
    start_tag = '<div data-elementor-type="wp-post"'
    end_tag = '<!-- .entry-content -->'
    
    pattern = re.compile(f'({start_tag}.*?){end_tag}', re.DOTALL)
    
    replacement_html = f'''<div class="product-details-content mb-5 mt-4">
        <h2>{data['title']}</h2>
        {data['content']}
    </div>
    <!-- .entry-content -->'''
    
    content = pattern.sub(replacement_html, content)

    # Write the modified content back
    with open(f"/opt/lampp/htdocs/Sethipipe/{filename}", "w") as f:
        f.write(content)
    
    print(f"Updated {filename}")
