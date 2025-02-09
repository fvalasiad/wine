# WinMM driver functions
@ stdcall -private DriverProc(long long long long long) OSS_DriverProc
@ stdcall -private auxMessage(long long long long long) OSS_auxMessage
@ stdcall -private midMessage(long long long long long) OSS_midMessage
@ stdcall -private modMessage(long long long long long) OSS_modMessage

# MMDevAPI driver functions
@ stdcall -private GetEndpointIDs(long ptr ptr ptr ptr) AUDDRV_GetEndpointIDs
@ stdcall -private GetAudioEndpoint(ptr ptr ptr) AUDDRV_GetAudioEndpoint
@ stdcall -private GetAudioSessionManager(ptr ptr) AUDDRV_GetAudioSessionManager
