import DaNgEr_MajoRLogin_pb2
from datetime import datetime
import os

def create_payload_with_version(version):

    major_login = DaNgEr_MajoRLogin_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = version  
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = "4306245793de86da425a52caadf21eed"
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    

    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = "4e79affe31414901544eaabebc4705738fe683a92dd4c5ee3db33662b2e9664f"
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    
    return major_login.SerializeToString()

def get_freefire_version():
    print("=" * 60)
    print("فري زبي للبايلود")
    print("=" * 60)
    print("OB52")
    print("=" * 60)
    print("\nاصدار")
    print("-" * 60)
    
    version = input("\nEnter Free Fire version: ").strip()
    

    while not version or version.count('.') < 2:
        print("\n✗ Invalid version format!")
        print("حط اصدار العبة الحالي 1.120.0)")
        version = input("\nEnter Free Fire version: ").strip()
    
    return version

def save_payload_file(hex_payload, version):

    safe_version = version.replace('.', '_')
    filename = f"ZZZZZZZZPPPPPPPPIIIIIIIIIIIIIIIIIII_{safe_version}.txt"
    

    with open(filename, 'w') as file:
        file.write(hex_payload)
    
    return filename

def main():

    try:

        freefire_version = get_freefire_version()
        
        print(f"\nحط اصدار العبة يا منيوك: {freefire_version}")
        
       
        payload_bytes = create_payload_with_version(freefire_version)
        
        hex_payload = payload_bytes.hex()
        
        filename = save_payload_file(hex_payload, freefire_version)
        
        
        print("\n" + "تممم" * 25)
        print("البايلود جهز يا منيوكه")
        print("" * 25)
        print(f"\n روح لملف زبي: {filename}")
        print(f" ملف {len(hex_payload)} characters")
        print(f" بايت: {len(payload_bytes)} bytes")
        print(f"\n ):")
        print("-" * 60)
        print(hex_payload)
        print("-" * 60)
        
        current_dir = os.path.abspath('.')
        print(f"\nNote: تم حفظ البايلود")
        print(f"{current_dir}")
        
    except ImportError:
        print("لم يوجد ملف")
        print("يتم تشفير")
        print("هناك ملف ناقص")
        
    except Exception as error:
        print(f"\nغلط {error}")
        print("خاطأ")

if __name__ == "__main__":

    main()