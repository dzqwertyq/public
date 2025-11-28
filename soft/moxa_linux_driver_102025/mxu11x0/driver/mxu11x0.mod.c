#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

#ifdef CONFIG_UNWINDER_ORC
#include <asm/orc_header.h>
ORC_HEADER;
#endif

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif



static const char ____versions[]
__used __section("__versions") =
	"\x18\x00\x00\x00\x64\xbd\x8f\xba"
	"_raw_spin_lock\0\0"
	"\x1c\x00\x00\x00\x34\x4b\xb5\xb5"
	"_raw_spin_unlock\0\0\0\0"
	"\x1c\x00\x00\x00\xa7\x75\x92\x1b"
	"__dynamic_dev_dbg\0\0\0"
	"\x28\x00\x00\x00\xc1\x46\x94\xe6"
	"__tty_insert_flip_string_flags\0\0"
	"\x20\x00\x00\x00\xce\xdb\xc0\x80"
	"tty_flip_buffer_push\0\0\0\0"
	"\x2c\x00\x00\x00\xc6\xfa\xb1\x54"
	"__ubsan_handle_load_invalid_value\0\0\0"
	"\x14\x00\x00\x00\x90\x24\xba\x71"
	"pcpu_hot\0\0\0\0"
	"\x10\x00\x00\x00\xa6\x50\xba\x15"
	"jiffies\0"
	"\x1c\x00\x00\x00\xad\x8a\xdd\x8d"
	"schedule_timeout\0\0\0\0"
	"\x20\x00\x00\x00\xd6\xc7\xd8\xaa"
	"default_wake_function\0\0\0"
	"\x18\x00\x00\x00\x38\x22\xfb\x4a"
	"add_wait_queue\0\0"
	"\x1c\x00\x00\x00\x88\x00\x11\x37"
	"remove_wait_queue\0\0\0"
	"\x1c\x00\x00\x00\x73\xe5\xd0\x6b"
	"down_interruptible\0\0"
	"\x0c\x00\x00\x00\x66\x69\x2a\xcf"
	"up\0\0"
	"\x18\x00\x00\x00\xc2\x9c\xc4\x13"
	"_copy_from_user\0"
	"\x20\x00\x00\x00\x5d\x7b\xc1\xe2"
	"__SCT__might_resched\0\0\0\0"
	"\x18\x00\x00\x00\x75\x79\x48\xfe"
	"init_wait_entry\0"
	"\x20\x00\x00\x00\x95\xd4\x26\x8c"
	"prepare_to_wait_event\0\0\0"
	"\x14\x00\x00\x00\xbf\x0f\x54\x92"
	"finish_wait\0"
	"\x18\x00\x00\x00\x86\xcc\x8f\x1f"
	"usb_clear_halt\0\0"
	"\x1c\x00\x00\x00\x07\x34\x37\xdd"
	"usb_set_interface\0\0\0"
	"\x14\x00\x00\x00\xbb\x6d\xfb\xbd"
	"__fentry__\0\0"
	"\x20\x00\x00\x00\x0b\x05\xdb\x34"
	"_raw_spin_lock_irqsave\0\0"
	"\x24\x00\x00\x00\x70\xce\x5c\xd3"
	"_raw_spin_unlock_irqrestore\0"
	"\x1c\x00\x00\x00\xca\x39\x82\x5b"
	"__x86_return_thunk\0\0"
	"\x24\x00\x00\x00\xd0\x48\xa7\x7c"
	"usb_serial_register_drivers\0"
	"\x10\x00\x00\x00\x7e\x3a\x2c\x12"
	"_printk\0"
	"\x14\x00\x00\x00\xaa\x27\x1b\x3a"
	"_dev_err\0\0\0\0"
	"\x18\x00\x00\x00\x76\x78\xa9\x95"
	"usb_submit_urb\0\0"
	"\x14\x00\x00\x00\x00\x0a\x3f\xdc"
	"tty_wakeup\0\0"
	"\x14\x00\x00\x00\x44\x43\x96\xe2"
	"__wake_up\0\0\0"
	"\x28\x00\x00\x00\xb3\x1c\xa2\x87"
	"__ubsan_handle_out_of_bounds\0\0\0\0"
	"\x20\x00\x00\x00\xd8\x94\xd3\x0b"
	"tty_termios_baud_rate\0\0\0"
	"\x18\x00\x00\x00\xe1\xbe\x10\x6b"
	"_copy_to_user\0\0\0"
	"\x1c\x00\x00\x00\xcb\xf6\xfd\xf0"
	"__stack_chk_fail\0\0\0\0"
	"\x18\x00\x00\x00\x30\x2b\x17\x6c"
	"usb_kill_urb\0\0\0\0"
	"\x28\x00\x00\x00\xf7\x01\x73\x51"
	"usb_serial_deregister_drivers\0\0\0"
	"\x18\x00\x00\x00\x20\x2e\xd1\x9e"
	"kmalloc_large\0\0\0"
	"\x10\x00\x00\x00\x38\xdf\xac\x69"
	"memcpy\0\0"
	"\x18\x00\x00\x00\x62\xa6\x98\xe1"
	"usb_bulk_msg\0\0\0\0"
	"\x10\x00\x00\x00\xba\x0c\x7a\x03"
	"kfree\0\0\0"
	"\x18\x00\x00\x00\x8c\x89\xd4\xcb"
	"fortify_panic\0\0\0"
	"\x1c\x00\x00\x00\x63\xa5\x03\x4c"
	"random_kmalloc_seed\0"
	"\x18\x00\x00\x00\x44\x99\xa9\x37"
	"kmalloc_caches\0\0"
	"\x18\x00\x00\x00\x04\x4f\xe1\x22"
	"kmalloc_trace\0\0\0"
	"\x18\x00\x00\x00\xe6\x18\x0c\xa8"
	"usb_match_id\0\0\0\0"
	"\x20\x00\x00\x00\xfe\x05\x50\xcc"
	"msleep_interruptible\0\0\0\0"
	"\x1c\x00\x00\x00\x30\xb9\xf4\x73"
	"usb_get_descriptor\0\0"
	"\x18\x00\x00\x00\x99\xd6\x39\x77"
	"usb_control_msg\0"
	"\x20\x00\x00\x00\x54\xea\xa5\xd9"
	"__init_waitqueue_head\0\0\0"
	"\x18\x00\x00\x00\x65\x83\x85\xfa"
	"module_layout\0\0\0"
	"\x00\x00\x00\x00\x00\x00\x00\x00";

MODULE_INFO(depends, "usbserial");

MODULE_ALIAS("usb:v110Ap7001d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap3001d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1131d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1151d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1150d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1130d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1110d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1110d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1130d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1150d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1151d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap1131d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap3001d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v110Ap7001d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "FCC70B6580601F589309EAA");
