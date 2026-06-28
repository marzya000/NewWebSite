/**
 * @author pxdraft
 * @version 1.0
 *
 */
(function($) {
    "use strict";
    var CRE = {};
    $.fn.exists = function() {
        return this.length > 0;
    };

    /* ---------------------------------------------- /*
     * Pre load
    /* ---------------------------------------------- */
    CRE.PreLoad = function() {
        document.getElementById("loading").style.display = "none";
    }

    /*--------------------
      * Menu toogle header
    ----------------------*/
    CRE.MenuToggleClass = function() {
        $('.navbar-toggler').on('click', function() {
            var toggle = $('.navbar-toggler').is(':visible');
            if (toggle) {
                $('header').toggleClass('header-toggle');
            }
        })
    }

    /* ---------------------------------------------- /*
     * Header Fixed
    /* ---------------------------------------------- */
    CRE.HeaderFixd = function() {
        var HscrollTop = $(window).scrollTop();
        var HHeight = $('.header-height').outerHeight()
        var HHeightTop = $('.header-top').outerHeight()
        
        if (HscrollTop >= 80) {
            $(".header-main:not(.no-header-fixed) .navbar-dark").addClass("navbar-light");
            $(".header-main:not(.no-header-fixed) .navbar-dark").addClass("navbar-dark-top");
            $(".header-main:not(.no-header-fixed) .navbar-dark-top").removeClass("navbar-dark");
            $(".header-main:not(.no-header-fixed)").addClass("fixed-header");
            $('.header-main:not(.no-header-fixed)').css("top", - HHeightTop);
        } else {
            $(".header-main:not(.no-header-fixed) .navbar-dark-top").removeClass("navbar-light");
            $(".header-main:not(.no-header-fixed) .navbar-dark-top").addClass("navbar-dark");
            $(".header-main:not(.no-header-fixed) .navbar-dark").removeClass("navbar-dark-top");
            $(".header-main:not(.no-header-fixed)").removeClass("fixed-header");
            $('.header-main:not(.no-header-fixed)').css("top", 0);
        }
    }


    /* ---------------------------------------------- /*
     * Header height
    /* ---------------------------------------------- */
    CRE.HeaderHeight = function() {
        var HHeight = $('.header-height').outerHeight()
        var HHeightTop = $('.header-top').outerHeight()
        $('.header-height-bar').css("min-height", HHeight);
    }

    /* ---------------------------------------------- /*
     * Mega Menu
    /* ---------------------------------------------- */

    CRE.MegaMenu = function() {
        var mDropdown = $(".px-dropdown-toggle") 
        mDropdown.on("click", function() {
            $(this).parent().toggleClass("open-menu-parent");
            $(this).next('.dropdown-menu').toggleClass("show");
            $(this).toggleClass("open");
        });
    }


    /*--------------------
    * Owl Corousel
    ----------------------*/
    CRE.Owl = function() {
        var owlslider = $("div.owl-carousel");
        if (owlslider.length > 0) {
            owlslider.each(function() {
                var $this = $(this),
                    $items = ($this.data('items')) ? $this.data('items') : 1,
                    $loop = ($this.attr('data-loop')) ? $this.data('loop') : true,
                    $navdots = ($this.data('nav-dots')) ? $this.data('nav-dots') : false,
                    $navarrow = ($this.data('nav-arrow')) ? $this.data('nav-arrow') : false,
                    $autoplay = ($this.attr('data-autoplay')) ? $this.data('autoplay') : true,
                    $autospeed = ($this.attr('data-autospeed')) ? $this.data('autospeed') : 5000,
                    $smartspeed = ($this.attr('data-smartspeed')) ? $this.data('smartspeed') : 1000,
                    $autohgt = ($this.data('autoheight')) ? $this.data('autoheight') : false,
                    $CenterSlider = ($this.data('center')) ? $this.data('center') : false,
                    $stage = ($this.attr('data-stage')) ? $this.data('stage') : 0,
                    $space = ($this.attr('data-space')) ? $this.data('space') : 30;

                $(this).owlCarousel({
                    loop: $loop,
                    items: $items,
                    responsive: {
                        0: {
                            items: $this.data('xs-items') ? $this.data('xs-items') : 1
                        },
                        576: {
                            items: $this.data('sm-items') ? $this.data('sm-items') : 1
                        },
                        768: {
                            items: $this.data('md-items') ? $this.data('md-items') : 1
                        },
                        992: {
                            items: $this.data('lg-items') ? $this.data('lg-items') : 1
                        },
                        1200: {
                            items: $items
                        }
                    },
                    dots: $navdots,
                    autoplayTimeout: $autospeed,
                    smartSpeed: $smartspeed,
                    autoHeight: $autohgt,
                    center: $CenterSlider,
                    margin: $space,
                    stagePadding: $stage,
                    nav: $navarrow,
                    navText: ["<i class='bi bi-chevron-left'></i>", "<i class='bi bi-chevron-right'></i>"],
                    autoplay: $autoplay,
                    autoplayHoverPause: true
                });
            });
        }
    }

    /* ---------------------------------------------- /*
     * lightbox gallery
    /* ---------------------------------------------- */
    CRE.Gallery = function() {
        var GalleryPopup = $('.lightbox-gallery');
        if (GalleryPopup.length > 0) {
            $('.lightbox-gallery').magnificPopup({
                delegate: '.gallery-link',
                type: 'image',
                tLoading: 'Loading image #%curr%...',
                mainClass: 'mfp-fade',
                fixedContentPos: true,
                closeBtnInside: false,
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0, 1] // Will preload 0 - before current, and 1 after CRE current image
                }
            });
        }
        var VideoPopup = $('.video-btn');
        if (VideoPopup.length > 0) {
            $('.video-btn').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false
            });
        }
    }

    /*--------------------
    * Masonry
    ----------------------*/
    CRE.masonry = function() {
        var portfolioWork = $('.post-masonry');
        if (portfolioWork.length > 0) {
            $(portfolioWork).isotope({
                resizable: false,
                itemSelector: '.grid-item',
                layoutMode: 'masonry',
                filter: '*'
            });
            //Filtering items on portfolio.html
            var portfolioFilter = $('.filter li');
            // filter items on button click
            $(portfolioFilter).on('click', function() {
                var filterValue = $(this).attr('data-filter');
                portfolioWork.isotope({
                    filter: filterValue
                });
            });
            //Add/remove class on filter list
            $(portfolioFilter).on('click', function() {
                $(this).addClass('active').siblings().removeClass('active');
            });
        }
    }


    /*--------------------
        * Parallax
    ----------------------*/
    CRE.parallax = function() {
        var Parallax = $('.parallax');
        if (Parallax.length > 0) {
            jarallax(document.querySelectorAll('.parallax'));
            /*jarallax(document.querySelectorAll('.parallax-img'), {
                keepImg: true,
            });*/
        }
    }

    // Window on Load
    $(window).on("load", function() {
        CRE.masonry(),
            CRE.PreLoad();
    });
    // Document on Ready
    $(document).ready(function() {
        CRE.HeaderFixd(),
        CRE.MenuToggleClass(),
        CRE.Gallery(),
        CRE.HeaderHeight(),
        CRE.parallax(),
        CRE.MegaMenu(),
        CRE.Owl();
    });

    // Document on Scrool
    $(window).scroll(function() {
        CRE.HeaderFixd();
    });

    // Window on Resize
    $(window).resize(function() {
        CRE.HeaderHeight();
    });

})(jQuery);